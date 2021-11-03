"Database utils for MySQL"
from MySQLdb.connections import Connection
from MySQLdb.cursors import Cursor


def connect() -> Connection:
    "Connect to MySQL and return Connection object."
    return Connection(
        host="mysql", port=3306, user="mysql", password="mysql", database="db"
    )


def get_cursor(conn: Connection) -> Cursor:
    "Get Cursor from MySQL Connection."
    return conn.cursor()
