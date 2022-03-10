from sqlalchemy import *
from sqlalchemy.orm import relationship

from hapi.models import Base

class PuissanceModel(Base):
    __tablename__= "puissance_c"
    idPuissance = Column(Integer, primary_key=True )
    nomPuissance=Column(String(255), unique=True, nullable=False)
    idCouleur=Column(Integer, ForeignKey('couleur.idCouleur'))
    
    region_c=relationship('RegionModel',
                          secondary='regionDePuissance',
                          back_populates='puissance_c')
    map=relationship(
        'MapModel',
        secondary='puissanceEtCarte',
        back_populates='puissance_c'
                      )
    disposition=relationship(
        'Disposition',
        secondary='categoriePuissance',
        back_populates='puissance_c'
                      )
    joueur=relationship(
        'Joueur',
        secondary='puissanceEtCarte',
        back_populates='puissance_c'
                      )
    unite=disposition=relationship('UniteModel')