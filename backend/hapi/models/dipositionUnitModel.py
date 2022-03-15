from sqlalchemy import *
from sqlalchemy.orm import relationship

from hapi.models import Base


class DispositionUnitModel(Base):
    __tablename__ = "disposition_unit"

     #Attributes
    id = Column(Integer, primary_key=True)
    type_unit_id = Column(Integer, ForeignKey('type_unit.id'))
    region_id = Column(Integer,ForeignKey('region.id'),primary_key=True)

    #Relationships
    type_unit = relationship("TypeUnitModel", back_populates='dispositions_unit')
    region = relationship("RegionModel", back_populates='dispositions_unit')
    
