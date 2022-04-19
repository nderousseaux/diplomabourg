from email.policy import default
from sqlalchemy import *
from sqlalchemy.orm import relationship

from hapi.models import *
from hapi.utils.validation import resolve_conflits

class OrderModel(Base):
    __tablename__ = "order"
    
    #Attributes
    id = Column(Integer, primary_key=True)
    type_order_id = Column(Integer, ForeignKey('type_order.id'))
    src_region_id = Column(Integer, ForeignKey('region.id'))
    dst_region_id = Column(Integer, ForeignKey('region.id'))
    unit_id = Column(Integer, ForeignKey('unit.id'))
    other_unit_id= Column(Integer, ForeignKey('unit.id'))
    is_valid= Column(Boolean ,default=False)
    num_tour = Column(Integer, nullable=False)
    state=Column(Boolean, default=True)

    #Relationships
    type_order=relationship('TypeOrderModel',  back_populates='orders')
    src_region=relationship('RegionModel', 
        primaryjoin="OrderModel.src_region_id == RegionModel.id",
        back_populates="orders_src_region")
    dst_region=relationship('RegionModel', 
        primaryjoin="OrderModel.dst_region_id == RegionModel.id",
        back_populates="orders_dst_region")
    unit=relationship("UnitModel", 
                    primaryjoin="OrderModel.unit_id==UnitModel.id",
                      back_populates='orders')
    other_unit=relationship("UnitModel",
                      primaryjoin="OrderModel.other_unit_id==UnitModel.id",
                      back_populates='orders_other_unit')

    """Teste si l'ordre s'effectue sur une unité qui nous appartient
    """              
    def is_on_my_unit(self):
        for u in self.dst_region.units_cur_region:
            if u.player == self.unit.player:
                return True
        return False

    """Teste si l'unité est aussi concernée dans un convoi
    """
    def exist_convoi(self):
        #Parmis tout les ordres de la partie et du joueur, on choppe ordre convoi
        ordres_convoi = [o for o in self.unit.player.orders() if o.other_unit_id == self]

        regions = []
        for o in ordres_convoi:
            regions.append(o.src_region)

        src = self.src_region
        i=0
        while i<len(regions):
            if region[i] in src.neighbours:
                src=listRegion[i]
                del listRegion[i]
                i=0
            else:
                i+=1
        if self.dst_region in src.neighbours:
            return True
        return False
    
    """Passe is_valid à true si l'ordre est cohérent
    """
    def validation(self):
        if self.type_order.name == "ATTACK":
            #Si je n'attaque pas une de mes unités
            if not self.is_on_my_unit():

                #Si c'est une unité terrestre
                if self.unit.type_unit.name == "ARMY": 
                    #Si c'est une région terrestre ou cotière
                    if (
                        "LAND" in [t.name for t in self.dst_region.types] or
                        "COAST" in [t.name for t in self.dst_region.types]
                    ):
                        #Si les régions sont connexes
                        if self.dst_region in self.src_region.neighbours:
                            self.is_valid = True
                            self.unit.cur_region_id=self.dst_region_id
                            return True

                        #Sinon il peut exister un convoi
                        elif self.exist_convoi():
                            self.is_valid = True
                            return True

                #Si c'est une flotte
                elif self.unit.type_unit.name == "FLOAT":
                    #Si c'est une région maritime ou cotière
                    if (
                        "SEA" in [t.name for t in self.dst_region.types] or
                        "COAST" in [t.name for t in self.dst_region.types]
                    ):
                        #Si les régions sont connexes
                        if self.dst_region in self.src_region.neighbours:
                            self.is_valid = True
                            self.unit.cur_region_id=self.dst_region_id
                            return True

        elif self.type_order.name == "CONVOY":            
            if (
                self.unit.type_unit.name == "FLOAT" and
                self.unit != self.other_unit and
                self.unit.type_unit.name == "ARMY" and
                "SEA" in [t.name for t in self.src_region.types] and
                "COAST" in [t.name for t in self.other_unit.cur_region] and
                "COAST" in [t.name for t in self.dst_region]
            ):      
                self.is_valid = True
                return True

        elif self.type_order.name == "SUPPORT":
            if self.unit.type_unit.name == "ARMY":
                if (
                    "SEA" in [t.name for t in self.dst_region.types] or
                    "COAST" in [t.name for t in self.dst_region.types]
                ):
                    if self.dst_region in self.src_region.neighbours:
                        self.is_valid = True
                        return True

            elif self.unit.type_unit.name == "FLEET":
                if (
                    "SEA" in [t.name for t in self.dst_region.types] or
                    "COAST" in [t.name for t in self.dst_region.types]
                ):
                    if self.dst_region in self.src_region.neighbours:
                        self.is_valid = True
                        return True
        self.is_valid = False
        return False

    """Coupe le soutient si la source est attaquée
    """
    def coupe_soutien(self):
        conflits = self.attackers_of_my_src()
        if len(conflits) == 0:
            self.state = False
        
    """Liste des ordres qui attaquent la source de l'ordre
    """
    def attackers_of_my_src(self):
        f = [o for o in self.unit.game.orders_valid() if (
            o is not self and
            o.type_order.name == "ATTACK" and
            o.dst_region is self.src_region
        )]
    
        return f

    """Romp un convoi si nécessaire
    """
    def broke_convoi(self):
        conflits = self.attackers_of_my_src()
        if len(conflits) != 0:
            orders = [c for c in conflit]
            orders.append(self)
            order_win = resolve_conflits(orders)
            if not order_win:
                self.state=False

    """Compte le nombre de soutient d'un ordre
    """
    def number_soutients(self):
        orders = [o for o in self.unit.game.orders_valid() if (
            o.type_order.name == "SUPPORT" and
            o.other_unit == self.unit
        )]
    
        return len(orders)

    """Supprime l'unité si elle doit l'être
    """
    def retrait(self):
        if len(self.src_region.units_cur_region) == 0:
            self.unit.cur_region = self.src_region
            
        else:    
          for n in self.dst_region.neighbours:
              if n != self.src_region:
                  if len(n.units_cur_region) == 0:
                      self.unit.cur_region=n
                      return True
        self.unit.life=False 
        return False
