from marshmallow import (
    Schema,
    fields,
    validate,
    pre_dump,
    post_load,
    pre_load,
    ValidationError,
    EXCLUDE
)
from hapi.models import DBSession, GameModel, PlayerModel

class PlayerSchema(Schema):
    id = fields.Int(dump_only=True)
    username=fields.Str(
        required=True,
        validate=[
            validate.Length(min=3, max=15, error="The len of username should be between 3 and 15")
        ]
    )
    is_admin = fields.Boolean()
    is_you = fields.Boolean(default=False)
    powers_id = fields.List(fields.Int())
    is_ready = fields.Boolean()

    class Meta:
        ordered = True
        unknown = EXCLUDE

    @post_load
    def post_load(self, data, **kwargs):
        return PlayerModel(**data)

    def check_username(self, player, game):

        player = DBSession().query(PlayerModel).filter_by(username=player.username).first()

        if player != None:
            raise ValidationError("The username provided is already use.", "username")

        return player
