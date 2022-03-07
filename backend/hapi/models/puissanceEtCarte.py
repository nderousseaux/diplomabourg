from sqlalchemy import *
from sqlalchemy.orm import relationship

from hapi.models import Base

puissanceEtCarte=Table(
    'puissanceEtCarte',
    Base.metadata,
    Column('idPuissance',ForeignKey('puissance_c.idPuissance')),
    Column('idCarte',ForeignKey('map.id')),
    
)