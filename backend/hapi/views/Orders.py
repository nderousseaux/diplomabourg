from cornice.resource import resource
import pyramid.httpexceptions as exception

from hapi.marshmallow_schemas import OrderSchema
from hapi.models import DBSession, OrderModel, GameModel, PlayerModel, UnitModel
from hapi.utils.auth import *
from hapi.utils.cors import cors_policy
from hapi.utils.service_informations import ServiceInformations


@resource(collection_path='/games/{game_id:\d+}/orders',path='/games/{game_id:\d+}/orders/{order_id:\d+}', cors_policy=cors_policy)
class Order():
    def __init__(self,request,context=None):
        self.request = request
        self.request.si = ServiceInformations(__name__, self.request)
        
        #on recupere gameId
        game_id=self.request.matchdict.get('game_id')

        order_id=self.request.matchdict.get('order_id')

        #on recupere le jeux qui a pour id game_id dans la BDD
        self.game=DBSession.query(GameModel).get(game_id)

        if(self.game==None):
            raise exception.HTTPNotFound()

        #On vérifie que la partie est en mode jeu
        if self.game.state.name != "GAME":
            raise exception.HTTPGone()

        
    def collection_get(self):
        check_member_of_game(self.request.user, self.game)
        
        #On récupère tous les ordres du joueur
        orders = self.request.user.orders()

        # Transformer les données en json
        data = OrderSchema(many=True).dump(orders)

        #On envoie la réponse
        return self.request.si.build_response(exception.HTTPOk, data)


    def collection_post(self):
        #On recupère les données
        newOrder = OrderSchema().load(self.request.json)

        if self.request.user != newOrder["unit"].player():
            raise exception.HTTPUnauthorized()

        #On récupère l'ordre si il existe
        order = DBSession.query(OrderModel)\
            .filter_by(unit=newOrder["unit"])\
            .filter_by(num_tour=self.game.num_tour)\
            .first()

        if order != None:
            for k, v in newOrder.items():
                setattr(order,k,v)
        else:
            order = OrderModel(**newOrder)

        order.num_tour = self.game.num_tour
        order.validation()

        DBSession().flush()
        return self.request.si.build_response(exception.HTTPOk, OrderSchema().dump(order))
        
