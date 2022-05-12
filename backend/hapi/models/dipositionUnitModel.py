from sqlalchemy import *
from sqlalchemy.orm import relationship

from hapi.models import Base


class DispositionUnitModel(Base):
    __tablename__ = "disposition_unit"

    #Attributes
    type_unit_id = Column(Integer, ForeignKey('type_unit.id'), primary_key=True)
    region_id = Column(Integer,ForeignKey('region.id'), primary_key=True)
    power_id=Column(Integer, ForeignKey('power.id'), primary_key=True)

    
    __table_args__ = (UniqueConstraint('region_id',name='region_uc'),)

    #Relationships
    type_unit = relationship("TypeUnitModel", back_populates='dispositions_unit')
    power = relationship('PowerModel',  back_populates="disposition_unit")
    region = relationship("RegionModel", back_populates='disposition_unit')