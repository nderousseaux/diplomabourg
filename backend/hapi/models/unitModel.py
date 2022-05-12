from sqlalchemy import *
from sqlalchemy.orm import relationship

from hapi.models import Base


class UnitModel(Base):
    __tablename__ = "unit"
    
    #Attributes
    id = Column(Integer, primary_key=True)
    type_unit_id = Column(Integer, ForeignKey('type_unit.id'))
    src_region_id = Column(Integer, ForeignKey('region.id'))
    cur_region_id = Column(Integer, ForeignKey('region.id'))
    life=Column(Boolean, default=True)
    power_id = Column(Integer, ForeignKey('power.id'))
    game_id = Column(Integer, ForeignKey('game.id'))
    
    #Relationships
    type_unit = relationship('TypeUnitModel',  back_populates='units')
    src_region=relationship('RegionModel', 
        primaryjoin="UnitModel.src_region_id == RegionModel.id",
        back_populates="units_src_region")
    cur_region=relationship('RegionModel', 
        primaryjoin="UnitModel.cur_region_id == RegionModel.id",
        back_populates="units_cur_region")
    power=relationship(
        'PowerModel',
        primaryjoin='foreign(UnitModel.power_id) == PowerModel.id',
        back_populates='units'   
    )
    orders=relationship('OrderModel',
                            primaryjoin="OrderModel.unit_id==UnitModel.id",
                            back_populates='unit')
    orders_other_unit=relationship('OrderModel',
                            primaryjoin="OrderModel.other_unit_id==UnitModel.id",
                            back_populates='other_unit')

    game=relationship('GameModel', back_populates="units")

    def player(self):
        players = [p for p in self.game.players if self.power in p.power]
        if len(players)>0:
            return players[0]
        return None