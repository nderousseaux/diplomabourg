<<<<<<< HEAD

=======
>>>>>>> 2b213c957b0a7f8cb1fd2280a97117ca00894d65
from sqlalchemy import *
from sqlalchemy.orm import relationship

from hapi.models import Base


class MapModel(Base):
    __tablename__ = "map"
    id = Column(Integer, primary_key=True)
<<<<<<< HEAD
    name = Column(String(255), unique=True, nullable=False)
    region_c=relationship('RegionModel',
                          secondary='regionDecarte',
                          back_populates='map')
    puissance_c=relationship('PuissanceModel',
                          secondary='puissanceETCarte',
                          back_populates='map')
    disposition=relationship('Disposition')
    partie=relationship('Partie')
=======
    name = Column(String(255), unique=True, nullable=False)
>>>>>>> 2b213c957b0a7f8cb1fd2280a97117ca00894d65
