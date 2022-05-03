from sqlalchemy import *
from sqlalchemy.orm import relationship
import pyramid.httpexceptions as exception

from hapi.models import Base, DBSession
from hapi.utils.validation import resolve_conflits

class GameModel(Base):
    __tablename__="game"

    #Attributes
    id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)
    password = Column(String(45), nullable=False)
    map_id = Column(Integer, ForeignKey('map.id'))
    state_id = Column(Integer, ForeignKey('state.id'), default=1)
    num_tour = Column(Integer, default=0)

    #Relationships
    map = relationship('MapModel', back_populates='games')
    state = relationship('StateModel', back_populates='games')
    players = relationship('PlayerModel',  back_populates='game')
    units = relationship('UnitModel', back_populates="game")

    def is_all_pret(self):
        if len([p for p in self.players if p.is_ready]) == len(self.players):
            return True
        return False
    
    def check_add_player(self, password):
        #On vérifie que la partie est toujours ouverte
        if self.state.name != "CONFIGURATION":
            raise exception.HTTPGone()

        #On vérifie que les mots de passes correspondent
        if self.password != password:
            raise exception.HTTPUnauthorized()

        #On vérifie que la partie n'est pas pleine
        if len(self.players) >= len(self.map.powers):
            raise exception.HTTPForbidden("Max number of players is reached")

    def orders(self):
        orders=[]
        for p in self.units:
            orders+=p.orders
        return [o for o in orders if o.num_tour == self.num_tour]

    def orders_valid(self):
        return [o for o in self.orders() if o.is_valid]

    """Parcourt tout les ordres et les valides, ou pas
    """
    def validation_orders(self):
        for o in self.orders():
            o.validation()
    
    """Retourne la liste de toutes les attaques mutuelles
    """
    def attaques_mutuelles(self):
        attaques = []
        redondance = []
        for o in [o for o in self.orders_valid() if o.type_order.name == "ATTACK"]:
            
            found = [o2 for o2 in self.orders() if (
                o2.type_order.name == "ATTACK" and
                o2 is not o and
                o2.src_region == o.dst_region and
                o2.dst_region == o.src_region
            )]
            
            if len(found)!=0:
                if o not in redondance:
                    redondance.append(o)

                    data=[]
                    data.append(o)
                    for f in found:
                        data.append(f)
                        redondance.append(f)
                        
                    attaques.append(data)  

        return attaques

    """Déplacement de toutes les unités
    """
    def move_units(self):
        for o in [o for o in self.orders_valid() if o.state]:
            o.unit.cur_region = o.dst_region
        

    def resolve_all_conflits(self):
        for l in self.conflicts():
            resolve_conflits(l)
        

    """Renvoie tout les ordres créant un conflit
    """
    def conflicts(self): 
        orders = self.orders()
        conflits = []
        ordres_conflits = []
    
        for o in orders:
            if o not in ordres_conflits:
                data = []
                data.append(o)
                ordres_conflits.append(o)
                for i in orders:
                    if o.id!=i.id and o.unit.cur_region==i.unit.cur_region:
                        data.append(i)
                        ordres_conflits.append(i)
                conflits.append(data)

        return conflits

    """Supprime les unités perdues
    """
    def remove_units_lost(self):
        for o in [o for o in self.orders() if not o.state]:
            o.retrait()
