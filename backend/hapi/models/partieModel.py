from sqlalchemy import *
from sqlalchemy.orm import relationship

from hapi.models import Base

class Partie(Base):
    __tablename__="partie"
    idPartie = Column(Integer, primary_key=True)
    nbJoueur= Column(Integer, unique=True, nullable=False)
    isStart=Column(String(45),nullable=False)
    nbTour =Column(Integer, nullable=False)
    idCarte=Column(Integer,ForeignKey('map.id'))
    duree=Column(Integer)
    joueur=relationship('Joueur')