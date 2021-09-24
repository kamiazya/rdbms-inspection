from MySQLdb.connections import Connection
from MySQLdb.cursors import Cursor


def connect() -> Connection:
    return Connection(
        host='mysql',
        port=3306,
        user='mysql',
        password='mysql',
        database='db')


def get_cursor(conn: Connection) -> Cursor:
    return conn.cursor()
