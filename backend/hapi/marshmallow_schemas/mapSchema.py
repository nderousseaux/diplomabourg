from marshmallow import (
    Schema,
    fields,
    validate,
    post_load,
    pre_load,
    EXCLUDE
)
from hapi.models import mapModel, DBSession

class MapSchema(Schema):
    id = fields.Int(dump_only=True)
    geojson = fields.Str()
    name = fields.Str(
        required=True,
        validate=validate.NoneOf("", error="Invalid value"),
        error_messages={
            "required": "This field is mandatory.",
            "null": "Field must not be null.",
        },
    )

    class Meta:
        ordered = True
        unknown = EXCLUDE

    @post_load
    def post_load(self, data, **kwargs):
        return mapModel(**data)

    @pre_load
    def pre_load(self, data, many, **kwargs):

        if "name" in data:
            map = DBSession().query(MapModel).filter_by(name=data["name"]).first()

            if map != None:
                raise ValueError("The given value '" + data["name"] + "' is already used.")

        return data











