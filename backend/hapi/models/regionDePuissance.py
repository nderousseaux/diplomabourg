from sqlalchemy import *
from sqlalchemy.orm import relationship

from hapi.models import Base

regionDePuissance=Table(
    'regionDePuissance',
    Base.metadata,
    Column('idPuissance',ForeignKey('puissance_c.idPuissance')),
    Column('idRegion',ForeignKey('region_c.idRegion')),
    Column('Unite',String(255)),
    Column('hasCenter',String(255)),
    
)