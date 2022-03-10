
from sqlalchemy import *
from sqlalchemy.orm import relationship

from hapi.models import Base


class OrdreModel(Base):
    
    __tablename__ = "ordre"
    idOrdre = Column(Integer, primary_key=True)
    typeOrdre=Column(Integer,ForeignKey('typeOrdre.idTypeOrdre'))
    idUnite=Column(INTEGER,nullable=False)
    idregionSource=Column(Integer)
    regionDestinanation=Column(Integer)
    
    joueur=Column(Integer,ForeignKey('joueur.idJoueur'))
    
   