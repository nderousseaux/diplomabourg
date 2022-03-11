from email import message
from sqlalchemy import *
from sqlalchemy.orm import relationship

from hapi.models import Base
from hapi.models.playerPowerModel import playerPowerModel


class PlayerModel(Base):
    __tablename__="player"

    #Attributes
    id = Column(Integer, primary_key=True)
    pseudo=Column(String(255), nullable=False)
    is_admin=Column(Boolean, nullable=False)
    game_id=Column(Integer ,ForeignKey('game.id'))
    
    #Relationships
    game = relationship('GameModel', backref='players')
    powers=relationship("PowerModel",
        secondary=playerPowerModel,
        back_populates="players"
    )
    units=relationship(
        "UnitsModel",
        primaryjoin='unit.player_power_player_id == player.id',
        back_populates='player'    
    )