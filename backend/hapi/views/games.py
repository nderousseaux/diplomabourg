from cornice.resource import resource
import pyramid.httpexceptions as exception

from hapi.marshmallow_schemas import JoinGameSchema, GameSchema
from hapi.models import DBSession, PlayerModel, GameModel, Base
from hapi.utils.auth import *
from hapi.utils.cors import cors_policy
from hapi.utils.service_informations import ServiceInformations

@resource(name="games", collection_path='/games', path="/games/{id_game:\d+}", cors_policy=cors_policy)
class Games():
    def __init__(self, request, context=None):
        self.request = request
        self.request.si = ServiceInformations(__name__, self.request)

        id_game = self.request.matchdict.get('id_game')
        if id_game != None:

            # On cherche la carte en db
            self.game = DBSession.query(GameModel).get(id_game)

            if self.game == None:
                raise exception.HTTPNotFound()

    # Getter une partie
    def get(self):
        #On vérifie que l'user connecté à bien accès à cette game
        check_member_of_game(self.request.user, self.game)

        # On transformme l'objet GameModel en JSON
        data = GameSchema().dump(self.game)

        #On envoie la réponse
        return self.request.si.build_response(exception.HTTPOk, data)

    #Créer une partie
    def collection_post(self):
        #On charge le body
        data = JoinGameSchema().load(self.request.json)

        #On ajoute les objets à la base
        data["game"] = GameModel(**data["game"])

        data["player"]["is_admin"] = True
        data["player"]["game"] = data["game"]
        data["player"] = PlayerModel(**data["player"])
        data["player"].is_you = True
        [DBSession().add(v) for v in data.values()]
        DBSession.flush()


        #On renvoie les infos
        res = {
            "token": self.request.create_jwt_token(data["player"].id),
            "game": GameSchema().dump(data['game'])
        }
        return self.request.si.build_response(exception.HTTPCreated(), res)

    #Modifier la partie
    def put(self):
        #On vérifier que l'utilisateur est bien administrateur
        check_admin_of_game(self.request.user, self.game)

        #On vérifie que la partie est toujours ouverte
        if self.game.state.name != "CONFIGURATION":
            raise exception.HTTPGone()

        #On récupère le body (pour vérifier l'intégrité des données)
        GameSchema(only=["name","password","map_id"]).load(self.request.json)

        #On modifie l'objet en base
        DBSession.query(GameModel).filter(GameModel.id == self.game.id).update(self.request.json)
        DBSession.flush()

        #On renvoie l'objet crée
        return self.request.si.build_response(exception.HTTPNoContent())