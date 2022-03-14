from marshmallow import (
    Schema,
    fields,
)

class RegionSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    types=fields.List(fields.Str())
    has_centre=fields.Boolean()

    
    class Meta:
        ordered = True