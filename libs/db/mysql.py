"Database utils for MySQL"
from MySQLdb.connections import Connection


def connect() -> Connection:
    "Connect to MySQL and return Connection object."
    return Connection(
        host="mysql", port=3306, user="mysql", password="mysql", database="db"
    )
