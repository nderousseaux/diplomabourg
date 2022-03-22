from marshmallow import (
    Schema,
    fields,
    EXCLUDE,
    post_load,
    pre_load
)

from hapi.marshmallow_schemas.unitSchema import UnitSchema
from hapi.marshmallow_schemas.regionSchema import RegionSchema

from hapi.models import DBSession, OrderModel, UnitModel, RegionModel

class OrderSchema(Schema):
    id = fields.Int(dump_only=True)
    type = fields.Str()
    unit_id = fields.Int()
    unit = fields.Nested(UnitSchema)
    region_id = fields.Int()
    region = fields.Nested(RegionSchema)
    is_valid = fields.Boolean()

    class Meta:
        ordered = True
        unknown = EXCLUDE

    @post_load
    def post_load(self, data, **kwargs):
        return OrderModel(**data)

    @pre_load
    def pre_load(self, data, **kwargs):
        if "unit_id" in data:
            unit = DBSession().query(UnitModel).get(data["unit_id"])

            if unit == None:
                raise ValidationError("Unit not found", "unit_id")
            else:
                data["unit"] = unit

        if "region_id" in data:
            region = DBSession().query(RegionModel).get(data["region_id"])

            if region == None:
                raise ValidationError("region not found", "region_id")
            else:
                data["region"] = region


        if "type" in data:
            unit = DBSession().query(UnitModel).filter(UnitModel.type_unit==data["type"]).first()


            if unit == None:
                raise ValidationError("Type not found", ["type"])
            else:
                data["type"] = unit


        return OrderModel(**data)