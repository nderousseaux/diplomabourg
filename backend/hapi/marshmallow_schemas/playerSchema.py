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
from hapi.models import DBSession, GameModel, PlayerModel, PowerModel
from hapi.marshmallow_schemas.powerSchema import PowerSchema
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
    powers = fields.List(fields.Nested(PowerSchema))

    class Meta:
        ordered = True
        unknown = EXCLUDE

    @pre_load
    def pre_load(self, data, **kwargs):
        if "powers_id" in data:
            data["powers"] = []
            for power_id in data["powers_id"]:
                power = DBSession().query(PowerModel).get(power_id)

                if power == None:
                    raise ValidationError("Power not found.", "powers_id")
                else: 
                    data["powers"].append(PowerSchema().dump(power))

            del data['powers_id']
        return data
    
    def check_powers(self, user, player):
        if "powers" in player:
            for power in player["powers"]:
                #On vérifie que les puissances appartiennent à la carte
                if power.id not in [p.id for p in user.game.map.powers]:
                    raise ValidationError("Power not associated with this map.", "powers_id")

                #On vérifie que les puissances sont disponibles 
                if not power.check_is_available(user):
                    raise ValidationError("Power is already selected by another player", "powers_id")


    def check_username(self, player, game, player_courrant=None):
        player = DBSession().query(PlayerModel)\
            .filter_by(username=player["username"])\
            .filter_by(game=game)\
            .first()

        if player != None:
            if player_courrant != None and player != player_courrant:
                raise ValidationError("The username provided is already use.", "username")

        return player

    def add_is_you(self, players, user):
        player = [p for p in players if p["id"] == user.id][0]
        player["is_you"] = True
        return players
