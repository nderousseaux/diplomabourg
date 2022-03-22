from sqlalchemy import *
from sqlalchemy.orm import relationship

from hapi.models import Base


class DispositionUnitModel(Base):
    __tablename__ = "disposition_unit"

     #Attributes
    id = Column(Integer, primary_key=True)
    type_unit_id = Column(Integer, ForeignKey('type_unit.id'))
    region_id = Column(Integer,ForeignKey('region.id'))
    power_id=Column(Integer, ForeignKey('power.id'))
    
    __table_args__ = (UniqueConstraint('region_id',name='region_uc'),
                     )

    #Relationships
    type_unit = relationship("TypeUnitModel", back_populates='dispositions_unit')
    
    power = relationship('PowerModel',  back_populates="disposition_unit")
    
    region = relationship("RegionModel", back_populates='disposition_unit')
    
    