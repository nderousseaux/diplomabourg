from sqlalchemy import *
from sqlalchemy.orm import relationship

from hapi.models import Base

class RegionModel(Base):
    __tablename__= "region_c"
    idRegion = Column(Integer, primary_key=True )
    
    nomRegion=Column(String(255), nullable=False ,unique=True)
    
    typeRegion=relationship(
        'TypeRegionModel',
         secondary='regionEtTypeRegion',
         back_populates='region_c'
    )
    
    map=relationship(
        'MapModel',
         secondary='regionDecarte',
         back_populates='region_c'
    )
    puissance_c=relationship('PuissanceModel',
                          secondary='regionDePuissance',
                          back_populates='region_c')
    voisin = relationship('RegionModel', remote_side=['idRegion'], backref='voisinRegion')
    
    unite=disposition=relationship('UniteModel')
    
    joueur=relationship('JoueurModel',
                          secondary='regionDeJoueur',
                          back_populates='region_c')