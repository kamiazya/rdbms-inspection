from contextlib import closing

import pytest
from MySQLdb.connections import Connection

from libs.db.mysql import connect
from libs.db.mysql import get_cursor
from models import Item


@pytest.fixture
def conn():
    with closing(connect()) as conn_:
        with closing(get_cursor(conn_)) as cur:
            Item.init(cur, drop=True)
        yield conn_


def test_save(conn: Connection):
    with closing(get_cursor(conn)) as cur:
        item = Item(name='test')
        item.save(cur)
        assert type(item.item_id) == int
