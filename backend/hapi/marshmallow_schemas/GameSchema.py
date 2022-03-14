from marshmallow import (
    Schema,
    fields,
    validate,
    post_load,
    pre_load,
    ValidationError,
    EXCLUDE
)
from hapi.marshmallow_schemas.mapSchema import MapSchema
from hapi.marshmallow_schemas import PlayerSchema
from hapi.models import DBSession, MapModel, GameModel

class GameSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(
        required=True,
        validate=[
            validate.Length(min=5, max=15, error="The len of name should be between 5 and 15")
        ]
    )
    password = fields.Str(
        validate=[
            validate.Length(min=5, max=15, error="The len of password should be between 5 and 15")
        ]
    )
    map=fields.Nested(MapSchema)
    map_id=fields.Int()
    state = fields.Str()
    players=fields.Nested(PlayerSchema)

    class Meta:
        ordered = True
        unknown = EXCLUDE

    
    @post_load
    def post_load(self, data, **kwargs):
        return gameModel(**data)

    @pre_load
    def pre_load(self, data, **kwargs):
        if "map_id" in data:
            map = DBSession().query(MapModel).get(data["map_id"])

            if map == None:
                raise ValidationError("Map not found", ["map_id"])
            else:
                data["map"] = map

        return gameModel(**data)


