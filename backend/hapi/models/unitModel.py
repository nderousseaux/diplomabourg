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
    player_power_power_id = Column(Integer, ForeignKey('player_power.power_id'))
    player_power_player_id = Column(Integer, ForeignKey('player_power.player_id'))
    
    #Relationships
    type_unit = relationship('TypeUnitModel',  back_populates='units')
    src_region=relationship('RegionModel', 
        primaryjoin="UnitModel.src_region_id == RegionModel.id",
        back_populates="units_src_region")
    cur_region=relationship('RegionModel', 
        primaryjoin="UnitModel.cur_region_id == RegionModel.id",
        back_populates="units_cur_region")
    player=relationship(
        'PlayerModel',
        primaryjoin='foreign(UnitModel.player_power_player_id) == PlayerModel.id',
        back_populates="units"
    )
    power=relationship(
        'PowerModel',
        primaryjoin='foreign(UnitModel.player_power_power_id) == PowerModel.id',
        back_populates='units'   
    )
    orders_unit=relationship('OrderModel',
                            primaryjoin="OrderModel.unit_id==UnitModel.id",
                            back_populates='unit')
    orders_other_unit=relationship('OrderModel',
                            primaryjoin="OrderModel.other_unit_id==UnitModel.id",
                            back_populates='other_unit')
