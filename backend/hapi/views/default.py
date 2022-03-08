from cornice import Service
from hapi.cors import cors_policy
import logging
log = logging.getLogger(__name__)


default = Service(name="default", path="/", cors_policy=cors_policy)

@default.get()
def my_view(request):
    log.info("Requesting route 'GET /'")

    return "Hello, world"