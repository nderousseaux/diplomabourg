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
    state_id = Column(Integer, ForeignKey('state.id'), default=1)
    nbtour = Column(Integer)

    #Relationships
    map = relationship('MapModel', back_populates='games')
    state = relationship('StateModel', back_populates='games')
    players = relationship('PlayerModel',  back_populates='game')

    def get_all_order(self):
        orders=[]
        for p in self.players :
            orders+=p.orders()
        return orders