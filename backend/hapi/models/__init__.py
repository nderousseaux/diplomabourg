import imp
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import scoped_session, sessionmaker

from zope.sqlalchemy import register

DBSession = scoped_session(sessionmaker())
register(DBSession)
Base = declarative_base()

from .colorModel import ColorModel
from .gameModel import GameModel
from .mapModel import MapModel
from .orderModel import OrderModel
from .playerModel import PlayerModel
from .powerModel import PowerModel
from .typeRegionModel import TypeRegionModel
from .regionModel import RegionModel
from .stateModel import StateModel
from .typeOrderModel import TypeOrderModel
from .typeUnitModel import TypeUnitModel
from .dipositionUnitModel import DispositionUnitModel
from .unitModel import UnitModel

from .typeRegionRegion import typeRegionRegion
from .playerPower import playerPower