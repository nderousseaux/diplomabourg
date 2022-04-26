from sqlalchemy import *
from sqlalchemy.orm import relationship

from hapi.models import Base

class RegionModel(Base):
    __tablename__= "region_c"
    idRegion = Column(Integer, primary_key=True )
    nomRegion=Column(String(255), unique=True, nullable=False)
    typeRegion=Column(String(255), nullable=False)
    map=relationship(
        'MapModel',
         secondary='regionDecarte',
         back_populates='region_c'
    )
    puissance_c=relationship('PuissanceModel',
                          secondary='regionDePuissance',
                          back_populates='region_c')
    
    # voisin = relationship(
    #                 'RegionModel',secondary='voisinRegion',
    #                 primaryjoin='idVosinSource.c.VolumeID'==idRegion,
    #                 secondaryjoin='idVoisinDestination.c.ParentID'==idRegion,
    #                 backref="children")
    voisin = relationship('RegionModel', remote_side=['idRegion'], backref='voisinRegion')