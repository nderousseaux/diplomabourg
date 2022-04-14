from cornice.resource import resource
from hapi.cors import cors_policy
import pyramid.httpexceptions as exception

from hapi.marshmallow_schemas.JoinGameSchema import JoinGameSchema
from hapi.marshmallow_schemas.GameSchema import GameSchema
from hapi.models import DBSession, PlayerModel, GameModel
from hapi.service_informations import ServiceInformations

@resource(name="games", collection_path='/games', path="/games/{idGame:\d+}", cors_policy=cors_policy)
class Games():
    def __init__(self, request, context=None):
        self.request = request
        self.request.si = ServiceInformations(__name__, self.request)

        idGame = self.request.matchdict.get('idGame')
        if idGame != None:

            # On cherche la carte en db
            self.game = DBSession.query(GameModel).get(idGame)

            if self.game == None:
                raise exception.HTTPNotFound()

    def get(self):
        #On vérifie que l'user connecté à bien accès à cette game
        if self.request.user == None or self.request.user.game != self.game:
            return self.request.si.build_response(
                exception.HTTPUnauthorized())



        # On transformme l'objet GameModel en JSON
        data = GameSchema().dump(self.game)

        #On envoie la réponse
        return self.request.si.build_response(exception.HTTPOk, data)

    def collection_post(self):
        #On charge le body
        data = JoinGameSchema().load(self.request.json)

        #On crée une nouvelle partie
        DBSession.add(data["game"])

        #On ajoute un joueur
        player = PlayerModel(**data["player"])
        player.is_admin = True
        data["game"].players.append(player)
        DBSession.add(player)
        DBSession.flush()

        #On renvoie les infos
        game = GameSchema().dump(data['game'])
        res = {
            "token": self.request.create_jwt_token(player.id),
            "game": GameSchema().add_is_you(game, player)
        }

        return self.request.si.build_response(exception.HTTPCreated(), res)

    def put(self):
        #On vérifie que l'user connecté à bien accès à cette game
        if self.request.user == None or self.request.user.game != self.game:
            return self.request.si.build_response(
                exception.HTTPUnauthorized())

        #On vérifie que l'user connecté à le droit de modier le player
        if not self.request.user.is_admin:
            return self.request.si.build_response(
                exception.HTTPUnauthorized())

         #On vérifie que la partie est toujours ouverte
        if self.game.state.name != "CONFIGURATION":
            return self.request.si.build_response(exception.HTTPGone())


        #On récupère le body (pour vérifier l'intégrité des données)
        GameSchema().load(self.request.json)

        #On modifie l'objet en base
        DBSession.query(GameModel).filter(GameModel.id == self.game.id).update(self.request.json)
        DBSession.flush()

        #On renvoie l'objet crée
        return self.request.si.build_response(exception.HTTPNoContent())