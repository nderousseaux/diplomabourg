import pyramid.httpexceptions as exception
from pyramid.config import Configurator
from pyramid.view import exception_view_config, notfound_view_config
from pyramid.authorization import ACLAuthorizationPolicy

from sqlalchemy import engine_from_config
from pyramid.renderers import JSON
from hapi.models import DBSession, Base, PlayerModel
from hapi.db_utils import load_engine
from hapi.service_informations import ServiceInformations

@notfound_view_config()
def notfound_view(request):
    return ServiceInformations("hapi", request).catch_error(exception.HTTPNotFound())

@exception_view_config(Exception)
def exception_view(request):
    return request.si.catch_error(request.exception)

def get_user(request):
    id = request.authenticated_userid
    if id is not None:
        try:
            user = DBSession().query(PlayerModel).\
                filter_by(id=id).one()
            return user
        except NoResultFound:
            return None

def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include("pyramid_tm")

    engine = load_engine(settings)
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    
    json_renderer = JSON()
    config.add_renderer("json", json_renderer)
    config.include("cornice")
    config.include('.routes')
    config.scan()

    config.set_authorization_policy(ACLAuthorizationPolicy())
    # Enable JWT authentication.
    config.include("pyramid_jwt")
    config.set_jwt_authentication_policy("secret", auth_type="Bearer", expiration=21600)

    config.add_request_method(get_user, "user", reify=True)


    return config.make_wsgi_app()