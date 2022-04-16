from sqlalchemy import *
from sqlalchemy.orm import relationship
import pyramid.httpexceptions as exception

from hapi.models import Base, DBSession
from hapi.models.unitModel import UnitModel

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

    def get_all_orders(self):
        orders=[]
        for p in self.players :
            orders+=p.orders
        return orders

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

    def place_units(self):
        dispositions = []
        for p in self.map.powers:
            for disp in p.disposition_unit:
                unit = UnitModel(
                    type_unit_id=disp.type_unit_id,
                    cur_region_id=disp.region_id,
                    power=p,
                    game=self,
                    src_region_id=disp.region_id
                )
                players = [play for play in p.players if play.game == self]
                if len(players)> 0:
                    unit.player = players[0]
            DBSession.add(unit)