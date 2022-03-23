from marshmallow import (
    Schema,
    fields,
    pre_dump
)

class RegionSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    types=fields.List(fields.Str())
    has_centre=fields.Boolean()

    
    class Meta:
        ordered = True