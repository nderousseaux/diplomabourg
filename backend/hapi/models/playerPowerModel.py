from sqlalchemy import *

from hapi.models import Base

playerPowerModel = Table('player_power', Base.metadata,
    Column('power_id', ForeignKey('power.id'), primary_key=True),
    Column('player_id', ForeignKey('player.id'), primary_key=True)
)