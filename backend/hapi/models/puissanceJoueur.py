from sqlalchemy import *
from sqlalchemy.orm import relationship

from hapi.models import Base


puissanceJoueur=Table(
    'puissanceJoueur',
    Base.metadata,
    Column('idPuissance',ForeignKey('puissance_c.idPuissance')),
    Column('idJoueur',ForeignKey('joueur.idJoueur')), 
)    