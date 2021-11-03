from contextlib import closing

from MySQLdb.connections import Connection
from ward import fixture
from ward import test

from libs.db.mysql import connect
from models import Item


@fixture
def connection():
    with closing(connect()) as conn_:
        yield conn_


@test("after executing save method, item_id is set.")
def _(conn: Connection = connection):
    item = Item(name="test")
    item.save(conn)
    assert type(item.item_id) == int
