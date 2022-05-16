import jwt 
import pyramid.httpexceptions as exception
import socketio

from hapi.utils.auth import get_user_by_id

sio = socketio.Server()

def init_sio(app):
    return socketio.WSGIApp(sio, app)


@sio.event
def connect(sid, environ, auth):
    try:
        id = jwt.decode(auth, "secret", algorithms=["HS512"])["sub"]
        user = get_user_by_id(id)
    except:
        raise exception.HTTPUnauthorized()
    
    sio.enter_room(sid, user.game.id)


def send_ping(game):
    """
    Envoie un ping à tout les joueurs de la game
    """
    sio.emit('ping', room=game.id)