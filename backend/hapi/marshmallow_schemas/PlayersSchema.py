from marshmallow import (
    Schema,
    fields,
    validate,
    post_load,
    pre_load,
    EXCLUDE
)


class PlayersSchema(Schema):
    name = fields.Str()
    isAdmin = fields.Boolean()



    class Meta:
        ordered = True
        unknown = EXCLUDE