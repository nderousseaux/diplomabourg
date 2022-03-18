from sqlalchemy import *
from sqlalchemy.orm import relationship

from hapi.models import Base
from hapi.models.playerPower import playerPower

class PowerModel(Base):
    __tablename__= "power"

    #Attributes
    id = Column(Integer, primary_key=True )
    name=Column(String(45), unique=False, nullable=False)
    color_id=Column(Integer, ForeignKey('color.id'))
    map_id=Column(Integer, ForeignKey('map.id'))

    #Relationships
    disposition_unit=relationship('DispositionUnitModel', back_populates="power")
    color=relationship('ColorModel', back_populates="powers")
    map=relationship('MapModel', back_populates="powers")
    dispositions=relationship('DispositionModel', 
        primaryjoin="DispositionModel.power_id==PowerModel.id",
        back_populates="power")

    players=relationship("PlayerModel",
        secondary=playerPower,
        back_populates="powers"
    )
    units=relationship("UnitModel", 
        primaryjoin='foreign(UnitModel.player_power_power_id) == PowerModel.id',
        back_populates="power"
    )
    