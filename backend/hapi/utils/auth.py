"""Fonctions utiles pour l'authentification dans les vues"""
import pyramid.httpexceptions as exception

from hapi.models import DBSession, PlayerModel


def get_user(request):
    id = request.authenticated_userid
    if id is not None:
        return get_user_by_id(id)
        
def get_user_by_id(id):
    try:
        user = DBSession().query(PlayerModel).\
            filter_by(id=id).one()

        user.is_you = True
        return user
    except NoResultFound:
            return None

def check_member_of_game(user, game):
    if user == None or user.game != game:
        raise exception.HTTPUnauthorized()

def check_admin_of_game(user, game):
    check_member_of_game(user, game)

    if not user.is_admin:
        raise exception.HTTPUnauthorized()

def check_can_update_player(user, player):
    check_member_of_game(user, player.game)
    
    if user != player and not user.is_admin:
        raise exception.HTTPUnauthorized()