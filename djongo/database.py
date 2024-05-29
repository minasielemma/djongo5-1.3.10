from logging import getLogger
from pymongo import MongoClient
from threading import Lock

logger = getLogger(__name__)
lock = Lock()

def connect(db, **kwargs):
    with lock:
        if db not in clients:
            logger.debug('New MongoClient connection')
            return  MongoClient(**kwargs, connect=False)


class Error(Exception):  # NOQA: StandardError undefined on PY3
    pass


class InterfaceError(Error):
    pass


class DatabaseError(Error):
    pass


class DataError(DatabaseError):
    pass


class OperationalError(DatabaseError):
    pass


class IntegrityError(DatabaseError):
    pass


class InternalError(DatabaseError):
    pass


class ProgrammingError(DatabaseError):
    pass


class NotSupportedError(DatabaseError):
    pass


def Binary(value):
    return value
