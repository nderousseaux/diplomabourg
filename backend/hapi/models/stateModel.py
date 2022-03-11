from sqlalchemy import *
from sqlalchemy.orm import relationship

from hapi.models import Base

class StateModel(Base):
    __tablename__="state"

    #Attributes
    id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)

    #Relationships
    games = relationship('GameModel', back_populates='state')