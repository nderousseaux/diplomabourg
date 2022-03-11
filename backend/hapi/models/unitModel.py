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
    player_power_power_id = Column(Integer, ForeignKey('player_power.power_id'))
    player_power_player_id = Column(Integer, ForeignKey('player_power.player_id'))
    
    #Relationships
    type_unit = relationship('TypeUnitModel', backref='units')
    src_region=relationship('RegionModel', backref="units_src_region")
    cur_region=relationship('RegionModel', backref="units_cur_region")
    player=relationship(
        'player',
        primaryjoin='unit.player_power_player_id == player.id',
        backref="units"
    )
    power=relationship(
        'power',
        primaryjoin='unit.player_power_power_id == power.id'
    )

