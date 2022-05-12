from marshmallow import (
    Schema,
    fields,
    post_load,
    ValidationError
)

from hapi.models import DBSession, OrderModel, UnitModel, RegionModel, TypeOrderModel

class OrderSchema(Schema):
    id = fields.Int(dump_only=True)
    type_order = fields.Str()
    unit_id = fields.Int()
    unit = fields.Nested("UnitSchema")
    other_unit_id = fields.Int()
    other_unit = fields.Nested("UnitSchema")
    src_region_id = fields.Int()
    dst_region_id = fields.Int(required=True) 
    src_region = fields.Nested("RegionSchema")
    dst_region = fields.Nested("RegionSchema")
    is_valid = fields.Boolean(default=False)
    num_tour = fields.Int() 

    @post_load
    def post_load(self, data, **kwargs):
        if "unit_id" in data:
            unit = DBSession().query(UnitModel).get(data["unit_id"])

            if unit == None:
                raise ValidationError("Unit not found", "unit_id")
            else:
                data["unit"] = unit
            
            del data["unit_id"]

        if "other_unit_id" in data:
            unit = DBSession().query(UnitModel).get(data["other_unit_id"])

            if unit == None:
                raise ValidationError("Unit not found", "other_unit_id")
            else:
                data["other_unit"] = unit
            
            del data["other_unit_id"]

        if "src_region_id" in data:
            region = DBSession().query(RegionModel).get(data["src_region_id"])

            if region == None:
                raise ValidationError("region not found", "src_region_id")
            else:
                data["src_region"] = region

            del data["src_region_id"]

        if "dst_region_id" in data:
            region = DBSession().query(RegionModel).get(data["dst_region_id"])

            if region == None:
                raise ValidationError("region not found", "dst_region_id")
            else:
                data["dst_region"] = region

            del data["dst_region_id"]
            

        if "type_order" in data:
            type_order = DBSession()\
                .query(TypeOrderModel)\
                .filter_by(name=data["type_order"])\
                .first()

            if type_order == None:
                raise ValidationError("type not found", "type_order")

            data["type_order"] = type_order

        return data
