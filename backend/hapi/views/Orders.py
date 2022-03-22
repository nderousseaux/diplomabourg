import collections
from cornice.resource import resource
from hapi.cors import cors_policy
import pyramid.httpexceptions as exception

from hapi.marshmallow_schemas import OrderSchema,GameSchema
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

            
        #je crée un joueur pour le test
        player = PlayerModel(username='joueur1', is_admin=False, game=self.game)
        DBSession.add(player)
        DBSession.flush()

        
        def collection_get(self):

            
            #la requet pour recuperer tous les ordres du joueur actuel

            Ordre=DBSession.query(OrderModel).join(UnitModel)\
                .filter(UnitModel.player_power_player_id==player)\
                    .all()

            # Transformer les donnée en json
            data = OrderSchema(many=True).dump(Order)

            #On envoie la réponse
            return self.request.si.build_response(exception.HTTPOk, data)


        def collection_post(sef):
            
            #on recupère les données
            data = OrderSchema().load(self.request.json)

            unit=DBSession.query(OrderModel).filter(OrderModel.unit_id==data["unit_id"]).first()

            if(unit!=None):
                unit.update(data)

            else:

                #On crée un ordre
                order=OrderModel(data)
                DBSession.add(order)
            #On renvoie l'objet crée

            DBSession.flush()
            return self.request.si.build_response(exception.HTTPOk, OrderSchema().dump(order))
           
