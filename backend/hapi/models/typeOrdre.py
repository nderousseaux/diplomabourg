from sqlalchemy import *
from sqlalchemy.orm import relationship

from hapi.models import Base


class TypeOrdreModel(Base):
    __tablename__ = "typeOrdre"
    idTypeOrdre = Column(Integer, primary_key=True)
    typeOrdre= Column(String(255), unique=True, nullable=False)
    ordre=relationship('OrdreModel')
    