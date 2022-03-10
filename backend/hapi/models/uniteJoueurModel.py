
from sqlalchemy import *
from sqlalchemy.orm import relationship

from hapi.models import Base


class UniteJoueurModel(Base):
    __tablename__ = "UniteJoueur"
    
    idUnite= Column(Integer, primary_key=True)
    
    idCategorieUnite=Column(Integer,ForeignKey('categorieUnite.idcategorieUnite'))
    
    idJoueur=Column(Integer,ForeignKey('joueur.idJoueur'))
    
    idRegionSource=Column(Integer,nullable=False)
    
    idRegionCourant=Column(Integer,nullable=False)
    
    