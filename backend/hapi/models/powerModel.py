from sqlalchemy import *
from sqlalchemy.orm import relationship

from hapi.models import Base
from hapi.models.playerPowerModel import playerPowerModel

class PowerModel(Base):
    __tablename__= "power"

    #Attributes
    id = Column(Integer, primary_key=True )
    name=Column(String(45), unique=False, nullable=False)
    color_id=Column(Integer, ForeignKey('color.id'))
    map_id=Column(Integer, ForeignKey('map.id'))

    #Relationships
    color=relationship('ColorModel', backref="powers")
    map=relationship('MapModel', backref="powers")
    regions=relationship('RegionModel', back_populates="power")
    dispositions=relationship('DispositionModel', back_populates="power")
    players=relationship("PlayerModel",
        secondary=playerPowerModel,
        back_populates="powers"
    )
