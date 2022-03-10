from sqlalchemy import *
from sqlalchemy.orm import relationship

from hapi.models import Base


class TypeRegionModel(Base):
    __tablename__ = "typeRegion"
    
    idTypeRegion = Column(Integer, primary_key=True)
    typeRegion = Column(String(255), unique=True, nullable=False)
    
    region=relationship('RegionModel',
                          secondary='regionEtTypeRegion',
                          back_populates='typeRegion')