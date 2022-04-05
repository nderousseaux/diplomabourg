from marshmallow import (
    Schema,
    fields,
    validate
)
from hapi.marshmallow_schemas.gameSchema import GameSchema, PlayerSchema

class JoinGameSchema(Schema):
    player = fields.Nested(PlayerSchema())
    game =fields.Nested(GameSchema())


    class Meta:
        ordered = True