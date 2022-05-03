from dotenv import load_dotenv
from pyramid.paster import get_appsettings, setup_logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
import os
import sys
import transaction

from hapi.data.minimal import insert_minimal_data
from hapi.data.test import insert_test_data
from hapi.models import *


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

    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    cleen(Base, session)

    insert_minimal_data(session)

    return session

def fill_test_data(argv=sys.argv):
    session = main()

    insert_test_data(session)

def cleen(Base, session):
    meta = Base.metadata
    for table in reversed(meta.sorted_tables):
        session.execute(table.delete())
    session.flush()
