
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import scoped_session, sessionmaker

from zope.sqlalchemy import register

DBSession = scoped_session(sessionmaker())
register(DBSession)
Base = declarative_base()

from .mapModel import MapModel

from .couleurModel import CouleurModel

from .categorieUniteModel import CategorieUniteModel

from .uniteModel import UniteModel

from .puissanceModel import PuissanceModel

from .typeRegionModel import TypeRegionModel

from .regionEtTypeRegion import regionEtTypeRegion

from .regionModel  import RegionModel



from .regionDeCarte import regionDeCarte

from .regionDePuissance import regionDePuissance

from .puissanceEtCarte  import puissanceEtCarte

from .dispositionModel import Disposition

from .categoriePuissance import categoriePuissance

from .partieModel import Partie

 
from .typeOrdre import TypeOrdreModel

from .joueurModel import Joueur

from .ordreModel import OrdreModel

from .uniteJoueurModel import UniteJoueurModel

from .regionDejoueur  import regionDeJoueur



from .puissanceJoueur import puissanceJoueur

from .ordreJoueur import ordreJoueur

from .chatModel import ChatModel

from .voisinRegion import voisinRegion
