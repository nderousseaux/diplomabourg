from pyramid.view import exception_view_config, notfound_view_config
import pyramid.httpexceptions as exception

from hapi.utils.service_informations import ServiceInformations
from hapi.utils.cors import cors_policy


@notfound_view_config()
def notfound_view(request):
    return ServiceInformations("hapi", request).catch_error(exception.HTTPNotFound())

@exception_view_config(exception.HTTPUnauthorized)
def unhauthorized_view(request):
    return ServiceInformations("hapi", request).catch_error(exception.HTTPUnauthorized())

@exception_view_config(exception.HTTPGone)
def gone_view(request):
    return ServiceInformations("hapi", request).catch_error(exception.HTTPGone())

@exception_view_config(Exception)
def exception_view(request):
    return ServiceInformations("hapi", request).catch_error(request.exception)