from cornice.resource import resource
import pyramid.httpexceptions as exception

from hapi.marshmallow_schemas import PlayerSchema, GameSchema
from hapi.models import GameModel, PlayerModel
from hapi.utils.auth import *
from hapi.utils.cors import cors_policy
from hapi.utils.service_informations import ServiceInformations
from hapi.utils.state import change_state
from hapi.utils.socket import send_ping


@resource(name="players", collection_path="/games/{id_game:\d+}/players", path="/games/{id_game:\d+}/players/{id_player:\d+}", cors_policy=cors_policy)
class Players():
    def __init__(self, request, context=None):
        self.request = request
        self.request.si = ServiceInformations(__name__, self.request)

        id_game = self.request.matchdict.get('id_game')

        # On cherche la carte en db
        self.game = DBSession.query(GameModel).get(id_game)

        if self.game == None:
            raise exception.HTTPNotFound()
        
        if "password" in self.request.params:
            self.password = self.request.params["password"]
        else:
            self.password = None

        #On vérifie que le player existe
        id_player = self.request.matchdict.get('id_player')

        if id_player != None:
            # On cherche le player en db
            self.player = DBSession.query(PlayerModel).get(id_player)

            #On vérifie que l'user appartient bien à cette carte
            if self.player.game != self.game:
                raise exception.HTTPNotFound()

            if self.player == None:
                raise exception.HTTPNotFound()

    #Get all users
    def collection_get(self):
        check_member_of_game(self.request.user, self.game)

        players = PlayerSchema().dump(self.game.players, many=True)

        return self.request.si.build_response(exception.HTTPOk(),players)

    #Créer un user (connection à une partie)
    def collection_post(self):
        #On charge le body
        data = PlayerSchema(only=["username"]).load(self.request.json)

        #On vérifie que l'username est pas déjà pris
        PlayerSchema().check_username(data, self.game)

        self.game.check_add_player(self.password)

        data = PlayerModel(**data)
        data.game = self.game
        data.is_you = True
        DBSession.flush()

        send_ping(self.game)

        res = {
            "token": self.request.create_jwt_token(data.id),
            "game": GameSchema().dump(self.game)
        }

        return self.request.si.build_response(exception.HTTPCreated(), res)

    #Modifier un user
    def put(self):
        check_can_update_player(self.request.user, self.player)

        newPlayer = PlayerSchema(only=["username", "power_id", "is_ready"]).load(self.request.json)

        if self.game.state.name != "CONFIGURATION":
            del newPlayer["username"]
            del newPlayer["power"]

        if "power" in newPlayer and len(newPlayer["power"]) == 0:
            newPlayer["power"] = self.player.power
    
        #On vérifie que l'username est pas déjà pris
        PlayerSchema().check_username(newPlayer, self.game, self.player)

        #On vérifie que la puissance n'est pas déjà prise
        PlayerSchema().check_power(newPlayer, self.game, self.player)

        #On modifie l'objet player      
        self.player.is_ready = False  
        for k, v in newPlayer.items():
            setattr(self.player,k,v)

        #On ne peut pas être pret si on a pas sélectionné de puissance
        if self.player.is_ready and len(self.player.power) == 0:
            self.player.is_ready = False

            raise exception.HTTPBadRequest("You cannot be ready : you don't have chose any power")
    
        DBSession().flush()

        #On vérifie si tout le monde est pret
        change_state(DBSession, self.game)
    
        send_ping(self.game)
        
        return self.request.si.build_response(exception.HTTPNoContent())