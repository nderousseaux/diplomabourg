import os
import sys
import transaction
import datetime

from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

from pyramid.paster import (
    get_appsettings,
    setup_logging,
)

from .models import (
    DBSession,
    Base,
)

from .models import *
from .models.regionModel import adjoining

from .models.data import *


from dotenv import load_dotenv

def usage(argv):
    cmd = os.path.basename(argv[0])
    print("usage: %s <config_uri>\n" '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)

def load_engine(settings):
    load_dotenv(settings['environment_file'])
    uri = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(
        os.getenv('MYSQL_USER'),
        os.getenv('MYSQL_PASSWORD'),
        os.getenv('MYSQL_HOST'),
        os.getenv('MYSQL_TCP_PORT'),
        os.getenv('MYSQL_DATABASE'),
    )
    engine = create_engine(uri)

    return engine

def pre(argv):
    if len(argv) != 2:
        usage(argv)
    os.system("env/bin/python setup.py develop && env/bin/python setup.py install")
    config_uri = argv[1]
    settings = get_appsettings(config_uri)
    engine = load_engine(settings)
    return engine



def main(argv=sys.argv):
    engine = pre(argv)
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)


def fill(argv=sys.argv):
    engine = pre(argv)
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    insertMaps(maps,session,MapModel)
    insertColor(colors,session,ColorModel)
    insertPower(powers,session,PowerModel)
    insertTypeRegion(typeRegion,session,TypeRegionModel)
    insertTypeUnite(typeUnite,session,TypeUnitModel)
    insertRegion(regions,session,RegionModel)
    insert_disposition_unite(dispositionUnite,session,DispositionUnitModel)
    insertion_voisin(voisinage,engine,adjoining)
    insertRegTypeReg(reg_type_reg,engine,typeRegionRegion)
    insertState(states,session,StateModel)
    insertTypeOrder(typeOders,session,TypeOrderModel)

    insertGame(games, session, GameModel)
    insertPlayer(players,session,PlayerModel)
    insertPlayerPower(playersPowers, engine, playerPower)
    insertUnite(unites, session, UnitModel)
    insertUnite(unitMaritimeConvoy, session, UnitModel)
    insertOrderAttack(orderAttack, session, OrderModel)
    insertOrderConvoy(orderConvoy, session, OrderModel)





    
    

    
   
