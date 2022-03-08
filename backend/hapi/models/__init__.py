from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import scoped_session, sessionmaker

from zope.sqlalchemy import register

DBSession = scoped_session(sessionmaker())
register(DBSession)
Base = declarative_base()

from .mapModel import MapModel
from .puissanceModel import PuissanceModel
from .regionModel  import RegionModel
from .regionDeCarte import regionDeCarte

from .regionDePuissance import regionDePuissance

from .puissanceEtCarte  import puissanceEtCarte

from .dispositionModel import Disposition

from .categoriePuissance import categoriePuissance

from .partieModel import Partie
from .joueurModel import Joueur
from .RegionDunJoueurModel import RegionDunJoueur
from .puissanceJoueur import puissanceJoueur
from .ordreModel import OrdreModel
from .ordreJoueur import ordreJoueur

from .chatModel import ChatModel

from .voisinRegion import voisinRegion
