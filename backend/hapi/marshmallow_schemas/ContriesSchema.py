from marshmallow import (
    Schema,
    fields,
    validate,
    post_load,
    pre_load,
    EXCLUDE
)

from hapi.marshmallow_schemas.RegionsSchema import RegionsSchema
from hapi.models import puissanceModel,DBSession

class ContriesSchema(Schema):
    id=fields.Int(dump_only=True)
    couleur=fields.Str()
    name=fields.Str(
        required=True,
        validate=validate.NoneOf("", error="Invalid value"),
        error_messages={
            "required": "This field is mandatory.",
            "null": "Field must not be null.",
        },
    )
    region=fields.Nested(RegionsSchema)


    class Meta:
        ordered = True
        unknown = EXCLUDE

    @post_load
    def post_load(self, data, **kwargs):
        return puissanceModel(**data)

    @pre_load
    def pre_load(self, data, many, **kwargs):

        if "name" in data:
            contrie = DBSession().query(puissanceModel).filter_by(name=data["name"]).first()

            if contrie != None:
                raise ValueError("The given value '" + data["name"] + "' is already used.")

        return data

