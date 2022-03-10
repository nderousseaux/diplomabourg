from sqlalchemy import *
from sqlalchemy.orm import relationship

from hapi.models import Base

regionDeJoueur=Table(
    'regionDeJoueur',
    Base.metadata,
    Column('idJoueur',ForeignKey('joueur.idJoueur')),
    Column('idRegion',ForeignKey('region_c.idRegion')),
    
)