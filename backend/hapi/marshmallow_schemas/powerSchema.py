from marshmallow import (
    Schema,
    fields,
)

class PowerSchema(Schema):
    id = fields.Int()
    name = fields.Str()

    # @post_load
    # def post_load(self, data, **kwargs):
    #     power = DBSession.query(PowerModel).get(data["id"])
    #     return power