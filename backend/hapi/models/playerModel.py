from email import message
from sqlalchemy import *
from sqlalchemy.orm import relationship

from hapi.models import Base
from hapi.models.playerPower import playerPower


class PlayerModel(Base):
    __tablename__="player"

    #Attributes
    id = Column(Integer, primary_key=True)
    username=Column(String(45), nullable=False)
    is_admin=Column(Boolean, nullable=False, default=False)
    game_id=Column(Integer ,ForeignKey('game.id'))
    is_ready=Column(Boolean, default=False)
    
    #Relationships
    game=relationship('GameModel', back_populates='players')
    power=relationship("PowerModel",
        secondary=playerPower,
        back_populates="players"
    )

    def orders(self):
        orders = []
        for unit in self.units:
            orders += unit.orders

        num_tour = self.game.num_tour    
        return [o for o in orders if o.num_tour == num_tour]

    def units(self):
        return [u for u in self.game.units() if u.player() == self]
