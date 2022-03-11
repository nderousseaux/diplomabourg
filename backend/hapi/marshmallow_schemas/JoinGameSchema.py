from marshmallow import (
    Schema,
    fields,
    validate,
    post_load,
    pre_load,
    EXCLUDE
)
from hapi.marshmallow_schemas.GameSchema import GameSchema

class JoinGameSchema(Schema):
    token = fields.Str()
    game =fields.Nested(GameSchema)


    class Meta:
        ordered = True
        unknown = EXCLUDE