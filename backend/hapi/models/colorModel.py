from sqlalchemy import *
from sqlalchemy.orm import relationship

from hapi.models import Base


class ColorModel(Base):
    __tablename__ = "color"

    #Attributes
    id = Column(Integer, primary_key=True)
    rgb= Column(String(45), unique=True, nullable=False)
    
    #Relationships
    powers=relationship('PowerModel', back_populates="color")