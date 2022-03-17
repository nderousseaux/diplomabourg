from marshmallow import (
    Schema,
    fields
)
from hapi.marshmallow_schemas.regionSchema import RegionSchema

class PowerSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    regions=fields.List(fields.Nested(RegionSchema))

    
    class Meta:
        ordered = True