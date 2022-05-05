from sqlalchemy import *
from sqlalchemy.orm import relationship

from hapi.models import Base

categoriePuissance=Table(
    'categoriePuissance',
    Base.metadata,
    Column('idPuissance',ForeignKey('puissance_c.idPuissance')),
    Column('idDisposition',ForeignKey('disposition.idDisposition')),
    Column('joueur',String(45),nullable=False)
)