from cornice.resource import resource
from hapi.cors import cors_policy
import pyramid.httpexceptions as exception

from hapi.marshmallow_schemas.joinGameSchema import JoinGameSchema
from hapi.marshmallow_schemas.gameSchema import GameSchema
from hapi.models import DBSession, PlayerModel, GameModel
from hapi.service_informations import ServiceInformations

@resource(name="games", collection_path='/games', path="/games/{idGame:\d+}", cors_policy=cors_policy)
class Games():
    def __init__(self, request, context=None):
        self.request = request
        self.request.si = ServiceInformations(__name__, self.request)

        idGame = self.request.matchdict.get('id')
        if idGame != None:

            # On cherche la carte en db
            self.game = DBSession.query(GameModel).get(idGame)

            if self.game == None:
                raise exception.HTTPNotFound()

    def collection_post(self):
        #On charge le body
        data = JoinGameSchema().load(self.request.json)

        #On crée une nouvelle partie
        DBSession.add(data["game"])

        #On ajoute un joueur
        data["player"].is_admin = True
        data["player"].game = data["game"]
        DBSession.add(data["player"])
        DBSession.flush()

        #On renvoie les infos
        game = GameSchema().dump(data["game"])
        res = {
            "token": self.request.create_jwt_token(data["player"].id),
            "game": GameSchema().add_is_you(game, data["player"])
        }

        return self.request.si.build_response(exception.HTTPCreated(), res)