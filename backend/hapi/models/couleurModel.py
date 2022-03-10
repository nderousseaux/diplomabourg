from sqlalchemy import *
from sqlalchemy.orm import relationship

from hapi.models import Base


class CouleurModel(Base):
    __tablename__ = "couleur"
    
    idCouleur = Column(Integer, primary_key=True)
    couleur= Column(String(255), unique=True, nullable=False)
    
    puissance=relationship('PuissanceModel')