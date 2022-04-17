import imp
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import scoped_session, sessionmaker

from zope.sqlalchemy import register


DBSession = scoped_session(sessionmaker())
register(DBSession)
Base = declarative_base()

from .colorModel import ColorModel
from .mapModel import MapModel
from .typeOrderModel import TypeOrderModel
from .stateModel import StateModel
from .dipositionUnitModel import DispositionUnitModel
from .regionModel import RegionModel
from .typeUnitModel import TypeUnitModel
from .powerModel import PowerModel
from .typeRegionModel import TypeRegionModel
from .orderModel import OrderModel
from .playerModel import PlayerModel
from .unitModel import UnitModel
from .gameModel import GameModel

from .typeRegionRegion import typeRegionRegion
from .playerPower import playerPower