from marshmallow import (
    Schema,
    fields,
    validate,
    post_load,
    pre_load,
    ValidationError
)

from hapi.models import DBSession, MapModel, GameModel

class GameSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(
        validate=[
            validate.Length(min=5, max=15, error="The len of name should be between 5 and 15")
        ]
    )
    password = fields.Str(
        validate=[
            validate.Length(min=5, max=15, error="The len of password should be between 5 and 15")
        ]
    )
    map=fields.Nested("MapSchema", dump_only=True)
    map_id=fields.Int(load_only=True)
    state = fields.Str(dump_only=True)
    players=fields.List(fields.Nested("PlayerSchema"), dump_only=True)
    num_tour=fields.Int()

    @pre_load
    def pre_load(self, data, **kwargs):
        #On vérifie que la carte existe
        if "map_id" in data:
            map = DBSession().query(MapModel).get(data["map_id"])

            if map == None:
                raise ValidationError("Map not found", "map_id")

        #On vérifie que le nom n'est pas déja pris
        if "name" in data:
            game = DBSession().query(GameModel).filter_by(name=data["name"]).first()

            if game != None:
                raise ValidationError("The name provided is already use.", "name")

        return data
