from sqlalchemy import *
from sqlalchemy.orm import relationship

from hapi.models import Base


class MapModel(Base):
    __tablename__ = "map"
    
    #Attributes
    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)

    #Relationships
    powers=relationship("PowerModel", back_populates="map") 
    games=relationship("GameModel", back_populates="map")