
from marshmallow import (
    Schema,
    fields,
    validate,
    post_load,
    pre_load,
    EXCLUDE
)

class RegionsSchema(Schema):
    id=fields.Int(dump_only=True)
    name=fields.Str()
    typeRegion=fields.Str()
    hasCentre=fields.Boolean()
