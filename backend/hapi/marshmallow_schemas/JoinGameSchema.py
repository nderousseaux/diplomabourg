from marshmallow import (
    Schema,
    fields,
    validate,
    post_load,
    pre_load,
    EXCLUDE
)

class JoinGameSchema(Schema):
    token = field.Str()
    game =field.Nested(GameSchema)