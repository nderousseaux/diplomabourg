from marshmallow import (
    Schema,
    fields
)
from hapi.models import mapModel, DBSession
from hapi.marshmallow_schemas import PowerSchema

class MapSchema(Schema):
    id = fields.Int(dump_only=True)
    geojson = fields.Str()
    name = fields.Str()
    powers = fields.Nested(PowerSchema)

    class Meta:
        ordered = True






