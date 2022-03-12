from sqlalchemy import *
from sqlalchemy.orm import relationship

from hapi.models import Base


class DispositionUniteModel(Base):
    __tablename__ = "dispositionUnite"
     #Attributes
    id = Column(Integer, primary_key=True)
    type_unit_id = Column(Integer, ForeignKey('type_unit.id'))

    idRegion=Column(Integer,ForeignKey('region.id'),unique=True)
    
