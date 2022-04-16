from marshmallow import (
    Schema,
    fields
)

from hapi.models import MapModel

class UnitSchema(Schema):
    id = fields.Int()
    type_unit = fields.Str()
    power_id = fields.Int()
    power = fields.Nested("PowerSchema")
    src_region_id = fields.Int()
    cur_region_id = fields.Int()
    player=fields.Nested("PlayerSchema")