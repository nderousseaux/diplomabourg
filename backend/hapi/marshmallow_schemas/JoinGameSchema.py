from marshmallow import (
    Schema,
    fields,
    validate
)
from hapi.marshmallow_schemas import GameSchema

class JoinGameSchema(Schema):
    username = fields.Str(
        validate=[
            validate.Length(min=3, max=15, error="The len of username should be between 3 and 15")
        ]
    )
    game =fields.Nested(GameSchema)


    class Meta:
        ordered = True