from sqlalchemy import *
from sqlalchemy.orm import relationship

from hapi.models import Base

voisinRegion=Table(
    'voisinRegion',
    Base.metadata,
    Column('idVosinSource',ForeignKey('region_c.idRegion')),
    Column('idVoisinDestination',ForeignKey('region_c.idRegion')),
    
)