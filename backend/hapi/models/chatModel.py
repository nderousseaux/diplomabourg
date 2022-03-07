from sqlalchemy import *
from sqlalchemy.orm import relationship

from hapi.models import Base


class ChatModel(Base):
    __tablename__ = "chat"
    id = Column(Integer, primary_key=True)
    texte= Column(String(255))
    idJoueur=Column(Integer,ForeignKey('joueur.idJoueur'))