
from marshmallow import (
    Schema,
    fields,
    validate,
    post_load,
    pre_load,
    EXCLUDE
)

from hapi.models import RegionModel,DBSession


class RegionsSchema(Schema):
    id=fields.Int(dump_only=True)
    name = fields.Str(
        required=True,
        validate=validate.NoneOf("", error="Invalid value"),
        error_messages={
            "required": "This field is mandatory.",
            "null": "Field must not be null.",
        },
    )
    typeRegion=fields.Str()
    hasCentre=fields.Boolean()

    
    class Meta:
        ordered = True
        unknown = EXCLUDE



    @post_load
    def post_load(self, data, **kwargs):
        return RegionModel(**data)

    @pre_load
    def pre_load(self, data, many, **kwargs):

        if "name" in data:
            region_l = DBSession().query(RegionModel).filter_by(name=data["name"]).first()

            if region_l!= None:
                raise ValueError("The given value '" + data["name"] + "' is already used.")

        return data


