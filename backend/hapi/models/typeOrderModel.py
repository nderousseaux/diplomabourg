from sqlalchemy import *
from sqlalchemy.orm import relationship

from hapi.models import Base


class TypeOrderModel(Base):
    __tablename__ = "type_order"
    
    #Attributes
    id = Column(Integer, primary_key=True)
    name = Column(String(45), unique=True, nullable=False)
    
    #Relationships
    orders=relationship('OrderModel', back_populates='type_order')

    def __str__(self):
        return self.name