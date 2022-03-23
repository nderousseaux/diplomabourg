from marshmallow import (
    Schema,
    fields,
)

from hapi.models import MapModel

class UnitSchema(Schema):
    id = fields.Int()
    type = fields.Str()
    power_id = fields.Int()
    src_region_id = fields.Int()
    cur_region_id = fields.Int()

    class Meta:
        ordered = True