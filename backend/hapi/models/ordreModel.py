
from sqlalchemy import *
from sqlalchemy.orm import relationship

from hapi.models import Base


class OrdreModel(Base):
    
    __tablename__ = "ordre"
    idOrdre = Column(Integer, primary_key=True)
    typeUnite = Column(String(255))
    typeOrdre=Column(String(255))
    regionSource=Column(String(255))
    regionDestinanation=Column(String(255))
    
    joueur=relationship(
        'Joueur',
        secondary='ordreJoueur',
        back_populates='ordre'
                      )