"""
Données de test
"""
from hapi.models import *

from .game_data import games
from .player_data import players
from .player_power_data import players_powers
from .unites_data import unites, unites_soutient, unites_maritime_convoy, unites_convoy_broken 
from .orders_data import orders_all

"""
Insertion des données de test
"""
def insert_test_data(session):
    for g in games:
        session.add(GameModel(**g))
    for p in players:
        session.add(PlayerModel(**p))
    for pp in players_powers:
        player = session.query(PlayerModel).get(pp["player_id"])
        power = session.query(PowerModel).get(pp["power_id"])
        player.power.append(power)
    for u in unites + unites_soutient + unites_maritime_convoy + unites_convoy_broken:
        session.add(UnitModel(**u))
    for o in orders_all:
        session.add(OrderModel(**o))

    session.commit()