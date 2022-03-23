from marshmallow import (
    Schema,
    fields,
    EXCLUDE,
    post_load,
    pre_load,
    ValidationError
)

from hapi.marshmallow_schemas.unitSchema import UnitSchema
from hapi.marshmallow_schemas.regionSchema import RegionSchema

from hapi.models import DBSession, OrderModel, UnitModel, RegionModel, TypeOrderModel

class OrderSchema(Schema):
    id = fields.Int(dump_only=True)
    type_order = fields.Str()
    unit_id = fields.Int()
    unit = fields.Nested(UnitSchema)
    src_region_id = fields.Int()
    region = fields.Nested(RegionSchema)
    is_valid = fields.Boolean(default=False)

    class Meta:
        ordered = True
        unknown = EXCLUDE

    @post_load
    def post_load(self, data, **kwargs):
        if "type_order" in data:
            type_order = DBSession()\
                .query(TypeOrderModel)\
                .filter_by(name=data["type_order"])\
                .first()

            if type_order == None:
                raise ValidationError("type not found", "type_order")


            data["type_order"] = type_order

        data["is_valid"] = False
        return data

    @pre_load
    def pre_load(self, data, **kwargs):
        if "unit_id" in data:
            unit = DBSession().query(UnitModel).get(data["unit_id"])

            if unit == None:
                raise ValidationError("Unit not found", "unit_id")

        if "src_region_id" in data:
            region = DBSession().query(RegionModel).get(data["src_region_id"])

            if region == None:
                raise ValidationError("region not found", "src_region_id")

        return data