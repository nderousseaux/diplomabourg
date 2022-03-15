from sqlalchemy import *
from sqlalchemy.orm import relationship

from hapi.models import Base

class DispositionModel(Base):
    __tablename__="disposition"
    
    #Attributes
    power_id=Column(Integer, ForeignKey('power.id'), primary_key=True)
    nbPlayer=Column(Integer, primary_key=True)
    player_index=Column(Integer, nullable=False)

    #Relationship
    power=relationship('PowerModel', 
        primaryjoin="PowerModel.id==DispositionModel.power_id",
        back_populates="dispositions")
