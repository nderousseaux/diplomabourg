from sqlalchemy import *
from sqlalchemy.orm import relationship

from hapi.models import Base

typeRegionRegion = Table(
    'type_region_region',
    Base.metadata,
    Column('region_id', Integer, ForeignKey('region.id')),
    Column('type_region_id',Integer, ForeignKey('type_region.id')),
)