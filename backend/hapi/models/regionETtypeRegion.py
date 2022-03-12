from sqlalchemy import *
from sqlalchemy.orm import relationship

from hapi.models import Base

regionEtTypeRegion=Table(
    'regionEtTypeRegion',
    Base.metadata,
    Column('idRegion',ForeignKey('region.id')),
    Column('idTypeRegion',ForeignKey('type_region.id')),
)
