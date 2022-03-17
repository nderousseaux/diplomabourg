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
    is_admin=Column(Boolean, nullable=False)
    game_id=Column(Integer ,ForeignKey('game.id'))
    is_ready=Column(Boolean, default=False)
    
    #Relationships
    game=relationship('GameModel', back_populates='players')
    powers=relationship("PowerModel",
        secondary=playerPower,
        back_populates="players"
    )
    units=relationship(
        "UnitModel",
        primaryjoin='foreign(UnitModel.player_power_player_id) == PlayerModel.id',
        back_populates='player'    
    )