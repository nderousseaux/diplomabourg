from sqlalchemy import *
from sqlalchemy.orm import relationship

from hapi.models import Base
from hapi.models.typeRegionRegion import typeRegionRegion

class TypeRegionModel(Base):
    __tablename__ = "type_region"
    
    #Attributes
    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)
    
    #Relationships
    regions=relationship('RegionModel',
        secondary=typeRegionRegion,
        back_populates='types')