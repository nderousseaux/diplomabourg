from marshmallow import (
    Schema,
    fields,
    validate,
    post_load,
    pre_load,
    EXCLUDE
)

class GameSchema(Schema):
    id=field.Int(dump_only=True)
    name=field.Str()
    password = field.Str()
    map=field.Nested(MapSchema)
    duration = field.Int()
    nbMaxPlayers = field.Int()
    state = field.Str()
    players=field.Nested(PlayersSchema)