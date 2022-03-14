from marshmallow import (
    Schema,
    fields
)
from hapi.marshmallow_schemas import RegionSchema

class PowerSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    regions=fields.List(fields.nested(RegionSchema))

    
    class Meta:
        ordered = True