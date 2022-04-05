from marshmallow import (
    Schema,
    fields,
    post_load
)
from hapi.models import DBSession, PowerModel
from hapi.marshmallow_schemas.regionSchema import RegionSchema

class PowerSchema(Schema):
    id = fields.Int()
    name = fields.Str()

    
    class Meta:
        ordered = True

    @post_load
    def post_load(self, data, **kwargs):
        power = DBSession.query(PowerModel).get(data["id"])
        return power