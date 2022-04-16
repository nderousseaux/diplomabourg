from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.config import Configurator
from pyramid.renderers import JSON
from sqlalchemy import engine_from_config

from hapi.models import DBSession, Base
from hapi.utils.auth import get_user
from hapi.utils.db import load_engine
from hapi.utils.service_informations import ServiceInformations

def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include("pyramid_tm")

    #Base de données
    engine = load_engine(settings)
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    
    #JSON Renderer
    json_renderer = JSON()
    config.add_renderer("json", json_renderer)

    #JWT Authentification
    config.set_authorization_policy(ACLAuthorizationPolicy())
    config.include("pyramid_jwt")
    config.set_jwt_authentication_policy("secret", auth_type="Bearer", expiration=21600)
    config.add_request_method(get_user, "user", reify=True)

    #Routes
    config.include("cornice")
    config.include('.routes')
    config.scan()

    return config.make_wsgi_app()
