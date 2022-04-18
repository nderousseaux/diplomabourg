from marshmallow import (
    Schema,
    fields,
    validate,
    post_load,
    ValidationError,
)

from hapi.models import DBSession, PlayerModel, PowerModel
from hapi.marshmallow_schemas.powerSchema import PowerSchema

class PlayerSchema(Schema):
    id = fields.Int(dump_only=True)
    username=fields.Str(
        validate=[
            validate.Length(min=3, max=15, error="The len of username should be between 3 and 15")
        ],
        required=True
        
    )
    is_admin = fields.Boolean(dump_only=True)
    is_you = fields.Boolean(dump_only=True)
    is_ready = fields.Boolean()
    power = fields.List(fields.Nested("PowerSchema", dump_only=True))
    power_id = fields.Int(load_only=True)

    @post_load
    def post_load(self, data, **kwargs):

        #On ajouter la puissance au player
        if "power_id" in data:
            power = DBSession().query(PowerModel).get(data["power_id"])

            if power == None:
                raise ValidationError("Power not found.", "powers_id")
            else: 
                data["power"]= [power]

            del data['power_id']

        return data


    def check_power(self, player, game, you=None):

        if "power" in player and len(player["power"]) > 0:

            #On vérifie que la puissance appartient à la carte
            if player["power"][0] not in game.map.powers:
                raise ValidationError("Power not associated with this map.", "powers_id")

            #On vérifie que la puissance est disponible
            if not player['power'][0].check_is_available(game, you):
                raise ValidationError("Power is already selected by another player", "powers_id")

    def check_username(self, player, game, you=None):
        if "username" in player:
            player = DBSession().query(PlayerModel)\
                .filter_by(username=player["username"])\
                .filter_by(game=game)\
                .first()

            if player != None and you != player:
                raise ValidationError("The username provided is already use.", "username")

        return player
