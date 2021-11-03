"Models for application"
from typing import Any
from typing import Optional

import aiosql
from MySQLdb.connections import Connection
from pydantic import BaseModel

from libs.db.adapter.pymysql import PyMySQLAdaptor


class DB:
    _queries: Any = aiosql.from_path("./init.sql", PyMySQLAdaptor)

    @classmethod
    def init(cls, conn: Connection) -> None:
        # pylint: disable=E1101
        cls._queries.init(conn)


class Item(BaseModel):
    item_id: Optional[int]
    name: str

    _queries: Any = aiosql.from_path("./items.sql", PyMySQLAdaptor)

    @classmethod
    def _insert(cls, conn: Connection, name: str) -> int:
        # pylint: disable=E1101
        return cls._queries.insert_item(conn, name=name)

    @classmethod
    def _update(cls, conn: Connection, item_id: int, name: str) -> int:
        # pylint: disable=E1101
        return cls._queries.update_item(conn, item_id=item_id, name=name)

    def save(self, conn: Connection):
        if self.item_id is None:
            self.item_id = self._insert(conn, self.name)
        else:
            self._update(conn, self.item_id, self.name)
