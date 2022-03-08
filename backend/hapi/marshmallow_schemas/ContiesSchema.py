from marshmallow import (
    Schema,
    fields,
    validate,
    post_load,
    pre_load,
    EXCLUDE
)

from hapi.marshmallow_schemas.RegionsSchema import RegionsSchema


class ContiesSchema(Schema):
    id=fields.Int(dump_only=True)
    couleur=fields.Str()
    name=fields.Str()
    region=fields.Nested(RegionsSchema)
