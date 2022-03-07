from sqlalchemy import *
from sqlalchemy.orm import relationship

from hapi.models import Base


ordreJoueur=Table(
    'ordreJoueur',
    Base.metadata,
    Column('idordre',ForeignKey('ordre.idOrdre')),
    Column('idJoueur',ForeignKey('joueur.idJoueur')),
    )