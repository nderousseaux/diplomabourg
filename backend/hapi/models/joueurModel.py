from email import message
from sqlalchemy import *
from sqlalchemy.orm import relationship

from hapi.models import Base

class Joueur(Base):
    __tablename__="joueur"
    idJoueur = Column(Integer, primary_key=True)
    pseudoJoueur=Column(String(255), unique=True, nullable=False)
    idPartie=Column(Integer ,ForeignKey('partie.idPartie'))
    state=Column(String(255)) # s'il est connecté ou pas 
    cookies=Column(String(255), unique=True)
    message=relationship('ChatModel')
    
    region=relationship('RegionDunJoueur')
    
    puissance_c=relationship('PuissanceModel',
                          secondary='puissanceJoueur',
                          back_populates='joueur')
    ordre=relationship('OrdreModel')
    
    uniteJoueur=relationship('UniteJoueur')
    
    region=relationship('RegionModel',
                          secondary='regionDeJoueur',
                          back_populates='joueur')
    