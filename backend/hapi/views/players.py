from cornice.resource import resource
from hapi.cors import cors_policy
import pyramid.httpexceptions as exception

from hapi.marshmallow_schemas.JoinGameSchema import PlayerSchema
from hapi.marshmallow_schemas.GameSchema import GameSchema
from hapi.models import DBSession, PlayerModel, GameModel
from hapi.service_informations import ServiceInformations


@resource(name="players", collection_path="/games/{idGame:\d+}/players", path="/games/{idGame:\d+}/players/{idPlayer:\d+}", cors_policy=cors_policy)
class Players():
    def __init__(self, request, context=None):
        self.request = request
        self.request.si = ServiceInformations(__name__, self.request)

        idGame = self.request.matchdict.get('idGame')

        # On cherche la carte en db
        self.game = DBSession.query(GameModel).get(idGame)

        if self.game == None:
            raise exception.HTTPNotFound()
        
        #On vérifie que le player existe
        idPlayer = self.request.matchdict.get('idPlayer')
        if idPlayer != None:
            # On cherche le player en db
            self.player = DBSession.query(PlayerModel).get(idPlayer)

            #On vérifie que l'user appartient bien à cette carte
            if self.player.game != self.game:
                raise exception.HTTPNotFound()

            if self.player == None:
                raise exception.HTTPNotFound()

    def collection_get(self):
        #On vérifie que l'user connecté à bien accès à cette game
        if self.request.user == None or self.request.user.game != self.game:
            return self.request.si.build_response(
                exception.HTTPUnauthorized())

        players = PlayerSchema().dump(self.game.players, many=True)

        return self.request.si.build_response(
            exception.HTTPOk(),
            PlayerSchema().add_is_you(players, self.request.user))

    def collection_post(self):
        #On charge le body
        data = PlayerSchema().load(self.request.json)

        #On vérifie que la partie est toujours ouverte
        if self.game.state.name != "CONFIGURATION":
            return self.request.si.build_response(exception.HTTPGone())

        #On vérifie que les mots de passes correspondent
        if self.game.password != self.request.params["password"]:
            return self.request.si.build_response(exception.HTTPUnauthorized())

        #On vérifie que la partie n'est pas pleine
        if len(self.game.players) >= len(self.game.map.powers):
            return self.request.si.build_response(exception.HTTPForbidden(), details="Max number of players is reached")

        #On vérifie que l'username est pas déjà pris
        PlayerSchema().check_username(data, self.game)
        
        #On ajoute un joueur
        player = PlayerModel(**data)
        player.game = self.game
        DBSession.add(player)
        DBSession.flush()

        #On renvoie les infos
        game = GameSchema().dump(self.game)
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
        if self.request.user != self.player and not self.request.user.is_admin:
            return self.request.si.build_response(
                exception.HTTPUnauthorized())

        newPlayer = PlayerSchema(
            only=["username", "powers", "is_ready"]
        ).load(self.request.json)
        
        #On vérifie que les powers appartiennent à la carte et sont disponible à la sélection
        PlayerSchema().check_powers(self.player, newPlayer)

        #On vérifie l'intégrité de l'username
        PlayerSchema().check_username(newPlayer, self.game, self.player)

        #On modifie l'objet player
        #On ajoute les powers
        if "powers" in newPlayer:
            powers = newPlayer.pop("powers")
            self.player.powers = powers
        DBSession.query(PlayerModel)\
            .filter_by(id=self.player.id)\
            .update(newPlayer)
        DBSession.flush()

        
        return self.request.si.build_response(exception.HTTPNoContent())