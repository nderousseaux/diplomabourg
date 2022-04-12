from sqlalchemy import *
from sqlalchemy.orm import relationship

from hapi.models import Base

class Disposition(Base):
    
    __tablename__="disposition"
    idDisposition=Column(Integer, primary_key=True)
    idCarte=Column(Integer,ForeignKey('map.id'))
    puissance_c=relationship('PuissanceModel',
                          secondary='categoriePuissance',
                          back_populates='disposition')
