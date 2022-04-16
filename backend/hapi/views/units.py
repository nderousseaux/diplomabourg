from cornice.resource import resource
import pyramid.httpexceptions as exception

from hapi.utils.cors import cors_policy
from hapi.marshmallow_schemas import UnitSchema
from hapi.utils.service_informations import ServiceInformations

@resource(name="units", collection_path='/units', path="/units/{id_unit:\d+}", cors_policy=cors_policy)
class Units():
    def __init__(self, request, context=None):
        self.request = request
        self.request.si = ServiceInformations(__name__, self.request)

        id_unit = self.request.matchdict.get('id_unit')
        if id_unit != None:

            # On cherche la carte en db
            self.unit = DBSession.query(UnitModel).get(id_unit)

            if self.unit == None:
                raise exception.HTTPNotFound()

    def collection_get(self):
        if self.request.user == None:
            raise exception.HTTPUnauthorized()
        
        data = UnitSchema().dump(self.request.user.game.units, many=True)

        #On envoie la réponse
        return self.request.si.build_response(exception.HTTPOk, data)