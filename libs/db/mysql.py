"Database utils for MySQL"
import os

from MySQLdb.connections import Connection

MYSQL_HOST = os.environ.get("MYSQL_HOST") or "mysql"


def connect() -> Connection:
    "Connect to MySQL and return Connection object."
    return Connection(
        host=MYSQL_HOST,
        port=3306,
        user="mysql",
        password="mysql",
        database="db",
    )
