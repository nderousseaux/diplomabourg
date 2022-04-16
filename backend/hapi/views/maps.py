from cornice.resource import resource
from hapi.utils.cors import cors_policy
import pyramid.httpexceptions as exception

from hapi.marshmallow_schemas import MapSchema
from hapi.models import MapModel, DBSession
from hapi.utils.service_informations import ServiceInformations

@resource(name="maps", collection_path='/maps', path='/maps/{id_map:\d+}', cors_policy=cors_policy)
class Maps():
    def __init__(self, request, context=None):
        self.request = request
        self.request.si = ServiceInformations(__name__, self.request)

        id_map = self.request.matchdict.get('id_map')
        if id_map != None:

            # On cherche la carte en db
            self.map = DBSession.query(MapModel).get(id_map)

            if self.map == None:
                raise exception.HTTPNotFound()

    def collection_get(self):
        #On cherche toutes les cartes en bdd
        maps = DBSession.query(MapModel).all()

        #On transformme l'objet MapModel en JSON
        data = MapSchema(many=True).dump(maps)

        #On envoie la réponse
        return self.request.si.build_response(exception.HTTPOk, data)

    def get(self):
        # On transformme l'objet MapModel en JSON
        data = MapSchema().dump(self.map)

        #On envoie la réponse
        return self.request.si.build_response(exception.HTTPOk, data)