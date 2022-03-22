from marshmallow import (
    Schema,
    fields
)
from hapi.models import mapModel, DBSession
from hapi.marshmallow_schemas.powerSchema import PowerSchema, RegionSchema

class MapSchema(Schema):
    id = fields.Int(dump_only=True)
    geojson = fields.Str()
    name = fields.Str()
    powers = fields.List(fields.Nested(PowerSchema))
    regions = fields.List(fields.Nested(RegionSchema))

    class Meta:
        ordered = True






