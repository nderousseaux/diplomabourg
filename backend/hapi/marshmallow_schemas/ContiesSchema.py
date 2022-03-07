from marshmallow import (
    Schema,
    fields,
    validate,
    post_load,
    pre_load,
    EXCLUDE
)


class ContiesSchema(Schema):
    id=field.Int(dump_only=True)
    couleur=field.Str()
    name=field.Str()
    region=field.Nested(RegionsSchema)
