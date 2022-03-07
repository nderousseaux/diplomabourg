from marshmallow import (
    Schema,
    fields,
    validate,
    post_load,
    pre_load,
    EXCLUDE
)


class PlayersSchema(Schema):
    name = field.Str()
    isAdmin = field.Boolean()