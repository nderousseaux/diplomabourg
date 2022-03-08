from marshmallow import (
    Schema,
    fields,
    validate,
    post_load,
    pre_load,
    EXCLUDE
)
from hapi.marshmallow_schemas.mapSchema import MapSchema
from hapi.marshmallow_schemas.PlayersSchema import PlayersSchema

class GameSchema(Schema):
    id=fields.Int(dump_only=True)
    name=fields.Str()
    password = fields.Str()
    map=fields.Nested(MapSchema)
    duration = fields.Int()
    nbMaxPlayers = fields.Int()
    state = fields.Str()
    players=fields.Nested(PlayersSchema)