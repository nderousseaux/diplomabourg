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

from .models.mapModel import MapModel

from dotenv import load_dotenv

def usage(argv):
    cmd = os.path.basename(argv[0])
    print("usage: %s <config_uri>\n" '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)

def load_engine(settings):
    load_dotenv(settings['environment_file'])
    engine = create_engine('mysql://{}:{}@{}:{}/{}'.format(
        os.getenv('MYSQL_USER'),
        os.getenv('MYSQL_PASSWORD'),
        os.getenv('MYSQL_HOST'),
        os.getenv('MYSQL_TCP_PORT'),
        os.getenv('MYSQL_DATABASE'),
    ))

    return engine

def pre(argv):
    if len(argv) != 2:
        usage(argv)
    os.system("python setup.py develop && python setup.py install")
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
    map1 = MapModel(name="Europe")
    session.add(map1)
    session.commit()
