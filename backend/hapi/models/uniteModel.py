from sqlalchemy import *
from sqlalchemy.orm import relationship

from hapi.models import Base


class UniteModel(Base):
    __tablename__ = "Unite"
    idUnite = Column(Integer, primary_key=True)
    
    
    idcategorieUnite = Column(Integer,ForeignKey('categorieUnite.idcategorieUnite'))
    
    idRegion=Column(Integer,ForeignKey('region_c.idRegion'))
    
    idPuissance=Column(Integer,ForeignKey('puissance_c.idPuissance'))
    
    