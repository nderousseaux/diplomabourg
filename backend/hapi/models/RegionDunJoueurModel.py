
from sqlalchemy import *
from sqlalchemy.orm import relationship

from hapi.models import Base


class RegionDunJoueur(Base):
    __tablename__ ="regionDunJoueur"
    idRegionJoueur = Column(Integer, primary_key=True)
    idJoueur = Column(Integer,ForeignKey('joueur.idJoueur'))
    nomRegion=Column(String(255), nullable=False)
    typeUnite=Column(String(255))
    hasCenter=Column(String(255))
    typeUnite=Column(String(255))
    