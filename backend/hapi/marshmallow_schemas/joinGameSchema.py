from marshmallow import (
    Schema,
    fields,
    validate
)
from hapi.marshmallow_schemas.GameSchema import GameSchema, PlayerSchema

class JoinGameSchema(Schema):
    player = fields.Nested(PlayerSchema())
    game =fields.Nested(GameSchema())


    class Meta:
        ordered = True