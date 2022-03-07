
from marshmallow import (
    Schema,
    fields,
    validate,
    post_load,
    pre_load,
    EXCLUDE
)

class RegionsSchema(Schema):
    id=field.Int(dump_only=True)
    name=field.Str()
    typeRegion=field.Str()
    hasCentre=fields.Boolean()
