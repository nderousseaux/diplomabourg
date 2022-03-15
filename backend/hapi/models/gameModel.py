from sqlalchemy import *
from sqlalchemy.orm import relationship

from hapi.models import Base

class GameModel(Base):
    __tablename__="game"

    #Attributes
    id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)
    password = Column(String(45), nullable=False)
    map_id = Column(Integer, ForeignKey('map.id'))
    state_id = Column(Integer, ForeignKey('state.id'))

    #Relationships
    map = relationship('MapModel', back_populates='games')
    state = relationship('StateModel', back_populates='games')
    players = relationship('PlayerModel',  back_populates='game')