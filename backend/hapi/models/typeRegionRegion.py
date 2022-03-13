from sqlalchemy import *
from sqlalchemy.orm import relationship

from hapi.models import Base

typeRegionRegion=Table(
    'type_region_region',
    Base.metadata,
    Column('idRegion',ForeignKey('region.id')),
    Column('idTypeRegion',ForeignKey('type_region.id')),
)
