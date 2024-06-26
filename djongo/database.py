from logging import getLogger
from pymongo import MongoClient
from threading import Lock

logger = getLogger(__name__)
lock = Lock()
mongo_client_instance:MongoClient = None

def connect(db, **kwargs):
    global mongo_client_instance
    with lock:
        if mongo_client_instance is None:
            logger.debug('New MongoClient connection')
            mongo_client_instance = MongoClient(**kwargs, connect=False)
            mongo_client_instance.max_pool_size = 1000000
            mongo_client_instance.max_idle_time_ms = 30000
        return mongo_client_instance


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
