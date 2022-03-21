from pyramid.response import Response
import pyramid.httpexceptions as exception
from marshmallow import ValidationError
import logging
import json

class ServiceInformations:

    def __init__(self, name, request):
        self.logger = logging.getLogger(name)
        self.request = request

    def log(self, response):
        data_log = {
            'client_addr': self.request.client_addr,
            'method': self.request.method,
            'path': self.request.path,
            'response_code' : response.status_code
        }

        #On ajoute le body si il existe
        try:
            data_log['body'] = self.request.json_body
        except:
            pass

        #On ajoute la réponse si elle existe
        try:
            data_log['response_content'] = response.json_body
        except:
            pass

        self.logger.info(data_log)

    def build_response(self, http_exception, data=None, message=None, details=None):
        response_content = data

        if  400 <= http_exception.code < 600:
            response_content = {
                "error": {
                    "status": http_exception.title.upper(),
                    "message": self.get_error_message_by_code(http_exception.code) if message == None else message,
                }
            }

            if details != None:
                response_content["error"].update({"details": details})


        response = Response(content_type="application/json")
        response.status_code = http_exception.code

        if response_content != None:
            response.json_body = response_content

        self.log(response)

        return response

    def catch_error(self, e):
        if type(e) is type(exception.HTTPNotFound()):
            response = self.build_response(exception.HTTPNotFound())

        else:
            try:
                raise e
            except ValidationError as validation_error:
                response = self.build_response(exception.HTTPBadRequest, None, validation_error.args)

            except ValueError as value_error:
                response = self.build_response(exception.HTTPBadRequest, None, str(value_error))

            except PermissionError as pe:
                response = self.build_response(exception.HTTPUnauthorized)

            except Exception as e:
                response = self.build_response(exception.HTTPInternalServerError)
                logging.getLogger(__name__).warn("Returning: %s", str(e))
        
        return response

    def get_error_message_by_code(self, code):

        switcher = {
            400: "Bad Request.",
            401: "Bad credentials.",
            403: "You do not have permission to perform this action.",
            404: "Requested resource is not found.",
            410: "Requested resource is no longer available",
            415: "Unsupported media type.",
            500: "The server encountred an internal error and was unable to complete your request.",
        }

        return switcher.get(code, "ERROR")