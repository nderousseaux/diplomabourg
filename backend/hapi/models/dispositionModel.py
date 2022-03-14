from sqlalchemy import *
from sqlalchemy.orm import relationship

from hapi.models import Base

class DispositionModel(Base):
    __tablename__="disposition"
    
    #Attributes
    nbPlayer=Column(Integer, primary_key=True)
    power_id=Column(Integer, ForeignKey('power.id'), primary_key=True)
    player_index=Column(Integer, nullable=False)

    #Relationship
    power=relationship('PowerModel', backref='dispositions')
