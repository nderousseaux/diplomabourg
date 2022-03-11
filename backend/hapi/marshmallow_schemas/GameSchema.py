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
from hapi.models import partieModel

class GameSchema(Schema):
    id=fields.Int(dump_only=True)
    name=fields.Str(
        required=True,
        validate=validate.NoneOf("",error="Invalid value"),
        error_messages={
            "required": "This field is mandatory.",
            "null": "Field must not be null.",
        },
        validate=validate.Length(min=2, max=40)
    )
    password = fields.Str()
    map=fields.Nested(MapSchema)
    duration = fields.Int(
        validete=validate.Length(max=100),error="max is 100")
    nbMaxPlayers = fields.Int(
        validete=validate.Length(min=2,max=7)),error="max  players is 7")
    )
    state = fields.Str()
    players=fields.Nested(PlayersSchema)


    class Meta:
        ordered = True
        unknown = EXCLUDE

    
    @post_load
    def post_load(self, data, **kwargs):
        return partieModel(**data)

   

