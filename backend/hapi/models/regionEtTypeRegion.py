from sqlalchemy import *
from sqlalchemy.orm import relationship

from hapi.models import Base

regionEtTypeRegion=Table(
    'regionEtTypeRegion',
    Base.metadata,
    Column('idRegion',ForeignKey('region_c.idRegion')),
    Column('idTypeRegion',ForeignKey('typeRegion.idTypeRegion')),
)