from logging import getLogger
from pymongo import MongoClient

logger = getLogger(__name__)
clients = {}

def is_connected(db):
    """
    Checks if the MongoClient connection for the given database is active.
    """
    try:
        client = clients[db]
        # The ismaster command is cheap and does not require auth.
        client.admin.command('ismaster')
        return True
    except Exception as e:
        logger.error(f"An unexpected error occurred while checking connection for {db}: {e}")
        return False


def connect(db, **kwargs):
    if db in clients and is_connected(db):
        return clients[db]
    clients[db] = MongoClient(**kwargs, connect=False)
    return clients[db]


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
