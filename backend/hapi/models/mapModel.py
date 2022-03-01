from sqlalchemy import *
from sqlalchemy.orm import relationship

from hapi.models import Base


class MapModel(Base):
    __tablename__ = "map"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)