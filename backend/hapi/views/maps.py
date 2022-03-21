from cornice.resource import resource
from hapi.cors import cors_policy
import pyramid.httpexceptions as exception

from hapi.marshmallow_schemas.mapSchema import MapSchema
from hapi.models import MapModel, DBSession
from hapi.service_informations import ServiceInformations

@resource(name="maps", collection_path='/maps', path='/maps/{id:\d+}', cors_policy=cors_policy)
class Maps():
    def __init__(self, request, context=None):
        self.request = request
        self.request.si = ServiceInformations(__name__, self.request)

        idMap = self.request.matchdict.get('id')
        if idMap != None:

            # On cherche la carte en db
            self.map = DBSession.query(MapModel).get(idMap)

            if self.map == None:
                raise exception.HTTPNotFound()

    def collection_get(self):
        #On cherhce tout les cartes en bdd
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

    def collection_post(self):
        #On récupère les données en post
        data = MapSchema().load(self.request.json)

        #On l'ajouter à la base
        DBSession.add(data)
        DBSession.flush()

        #On renvoie l'objet crée
        return self.request.si.build_response(exception.HTTPOk, MapSchema().dump(data))

    def put(self):
        #On récupère le body (pour vérifier l'intégrité des données)
        MapSchema().load(self.request.json)

        #On modifie l'objet en base
        DBSession.query(MapModel).filter(MapModel.id == self.map.id).update(self.request.json)
        DBSession.flush()

        #On renvoie l'objet crée
        return self.request.si.build_response(exception.HTTPNoContent())

    def delete(self):
        #On supprime l'objet en base
        DBSession.delete(self.map)
        DBSession.flush()

        #On renvoie l'objet crée
        return self.request.si.build_response(exception.HTTPNoContent())