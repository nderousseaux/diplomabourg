from marshmallow import (
    Schema,
    fields
)

class RegionSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    types=fields.List(fields.Str())
    has_centre=fields.Boolean()