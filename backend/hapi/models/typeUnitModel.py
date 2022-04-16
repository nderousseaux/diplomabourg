from sqlalchemy import *
from sqlalchemy.orm import relationship

from hapi.models import Base


class TypeUnitModel(Base):
    __tablename__ = "type_unit"
    
    #Attributes
    id = Column(Integer, primary_key=True)
    name = Column(String(45), unique=True, nullable=False)
    
    #Relationships
    units=relationship('UnitModel',
        back_populates='type_unit')
    dispositions_unit=relationship('DispositionUnitModel',  back_populates='type_unit')

    def __str__(self):
        return self.name