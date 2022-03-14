from marshmallow import (
    Schema,
    fields,
)
from hapi.marshmallow_schemas.mapSchema import MapSchema
from hapi.marshmallow_schemas import PlayerSchema
from hapi.models import MapModel

class UnitSchema(Schema):
    id = fields.Int(dump_only=True)
    type = fields.Str()
    power_id = fields.Int()
    src_region_id = fields.Int()
    cur_region_id = fields.Int()

    class Meta:
        ordered = True