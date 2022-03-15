from marshmallow import (
    Schema,
    fields,
    validate
)


class PlayerSchema(Schema):
    id = fields.Int(dump_only=True)
    username=fields.Str(
        required=True,
        validate=[
            validate.Length(min=3, max=15, error="The len of username should be between 3 and 15")
        ]
    )
    is_admin = fields.Boolean()
    is_you = fields.Boolean()
    powers_id = fields.List(fields.Int())
    is_ready = fields.Boolean()

    class Meta:
        ordered = True
        unknown = EXCLUDE
