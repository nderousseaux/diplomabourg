import collections
from cornice.resource import resource
from hapi.cors import cors_policy
import pyramid.httpexceptions as exception

from hapi.marshmallow_schemas.orderSchema import OrderSchema
from hapi.marshmallow_schemas.GameSchema import GameSchema
from hapi.models import OrderModel,GameModel,PlayerModel,UnitModel,DBSession
from hapi.service_informations import ServiceInformations


@resource(collection_path='/games/{gameId:\d+}/orders',path='/games/{gameId:\d+}/orders/{orderId:\d+}')
class Order():
    def __init__(self,request,context=None):
        self.request = request
        self.request.si = ServiceInformations(__name__, self.request)
        

        #on recupere gameId
        gameId=self.request.matchdict.get('gameId')
        orderId=self.request.matchdict.get('orderId')

        #on recupere le jeux qui a pour id gameId dans la BDD
        self.game=DBSession.query(GameModel).get(gameId)

        if(self.game==None):
            raise exception.HTTPNotFound()

        #je crée un joueur pour le test #FIXME: Vérifier user
        
    def collection_get(self):
        #On vérifie que l'user connecté à bien accès à cette game
        if self.request.user == None or self.request.user.game != self.game:
            return self.request.si.build_response(
                exception.HTTPUnauthorized())

        #On récupère tous les ordres du joueur
        orders = self.request.user.orders()

        # Transformer les données en json
        data = OrderSchema(many=True).dump(orders)

        #On envoie la réponse
        return self.request.si.build_response(exception.HTTPOk, data)


    def collection_post(self):
        #On recupère les données
        newOrder = OrderSchema(
            only=["type_order", "src_region_id", "unit_id", "is_valid"]
        ).load(self.request.json)

        #On récupère l'ordre si il existe
        order = DBSession.query(OrderModel)\
            .filter_by(unit_id=newOrder["unit_id"])\
            .first()

        if(order!=None):
            DBSession.query(OrderModel)\
                .filter_by(id=order.id)\
                .delete()

        #On crée un ordre
        order=OrderModel(**newOrder)
        DBSession.add(order)
        DBSession.flush()

        #On renvoie l'objet crée
        return self.request.si.build_response(exception.HTTPOk, OrderSchema().dump(order))
        
