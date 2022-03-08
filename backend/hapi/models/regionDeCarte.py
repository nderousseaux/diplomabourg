from sqlalchemy import *
from sqlalchemy.orm import relationship

from hapi.models import Base

regionDeCarte=Table(
    'regionDecarte',
    Base.metadata,
    Column('idCarte',ForeignKey('map.id')),
    Column('idRegion',ForeignKey('region_c.idRegion'))
)
    