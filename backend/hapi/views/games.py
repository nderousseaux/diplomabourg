from cornice.resource import resource
from hapi.cors import cors_policy
import pyramid.httpexceptions as exception

from hapi.marshmallow_schemas.joinGameSchema import JoinGameSchema
from hapi.marshmallow_schemas.gameSchema import GameSchema
from hapi.models import DBSession, PlayerModel
from hapi.service_informations import ServiceInformations

@resource(collection_path='/games', path='/games/{id:\d+}', cors_policy=cors_policy)
class Games():
    def __init__(self, request, context=None):
        self.request = request
        self.request.si = ServiceInformations(__name__, self.request)

    def collection_post(self):
        #On charge le body
        data = JoinGameSchema().load(self.request.json)

        #On crée une nouvelle partie
        DBSession.add(data["game"])
        #On ajoute un joueur
        player = PlayerModel(username=data["username"], is_admin=True, game=data["game"])
        DBSession.add(player)
        DBSession.flush()

        #On renvoie les infos
        game = GameSchema().dump(data["game"])
        game["players"][0]["is_you"] = True
        res = {
            "token": self.request.create_jwt_token(player.id),
            "game": game
        }

        return self.request.si.build_response(exception.HTTPCreated(), res)