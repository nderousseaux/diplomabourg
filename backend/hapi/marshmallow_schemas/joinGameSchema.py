from marshmallow import (
    Schema,
    fields,
    post_load
)

class JoinGameSchema(Schema):
    player = fields.Nested("PlayerSchema", only=["username"])
    game =fields.Nested("GameSchema", only=["name", "password", "map_id"])


    @post_load
    def post_load(self, data, **kwargs):
        data["player"]["game"] = data["game"]
        return data
