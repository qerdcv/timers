import os
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

ENGINE = None
CONNECTION = None
SESSION = None
# BASE_URL = f'postgresql://admin:admin@0.0.0.0/timer_data'
BASE_URL = 'sqlite:///:memory'


def engine():
    global ENGINE
    if ENGINE is None:
        ENGINE = create_engine(BASE_URL, echo=True)
    return ENGINE


def connection():
    global CONNECTION
    if CONNECTION is None:
        CONNECTION = engine().connect()
    return CONNECTION


@contextmanager
def session() -> Session:
    global SESSION
    if SESSION is None:
        SESSION = sessionmaker(bind=engine())
    s = SESSION()
    yield s

