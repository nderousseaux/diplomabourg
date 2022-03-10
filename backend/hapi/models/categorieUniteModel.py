from sqlalchemy import *
from sqlalchemy.orm import relationship

from hapi.models import Base


class CategorieUniteModel(Base):
    __tablename__ = "categorieUnite"
    idcategorieUnite = Column(Integer, primary_key=True)
    typeUnite= Column(String(255), unique=True, nullable=False)
    
    unite=relationship('UniteModel')
    
    uniteJoueur=relationship('UniteJoueur')