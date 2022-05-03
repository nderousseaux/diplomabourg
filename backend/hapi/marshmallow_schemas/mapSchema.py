from marshmallow import (
    Schema,
    fields
)

class MapSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    powers = fields.List(fields.Nested("PowerSchema"))
    regions = fields.List(fields.Nested("RegionSchema"))






