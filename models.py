"Models for application"
from typing import Optional

from MySQLdb.cursors import Cursor
from pydantic import BaseModel


class Item(BaseModel):
    item_id: Optional[int]
    name: str

    class _query:

        drop_table = "DROP TABLE IF EXISTS items;"

        create_table = (
            "CREATE TABLE IF NOT EXISTS items ("
            "  item_id INT(11) NOT NULL AUTO_INCREMENT,"
            "  name VARCHAR(100),"
            "  PRIMARY KEY (item_id)"
            ");"
        )

        insert = "INSERT INTO items (name) VALUES (%s);"
        update = "UPDATE items SET name = %s WHERE item_id = %s;"

    @staticmethod
    def _create_table(cur: Cursor) -> None:
        print(Item._query.create_table)
        cur.execute(Item._query.create_table)

    @staticmethod
    def _drop_table(cur: Cursor) -> None:
        print(Item._query.drop_table)
        cur.execute(Item._query.drop_table)

    @classmethod
    def init(cls, cur: Cursor, drop: bool = False) -> None:
        if drop:
            cls._drop_table(cur)
        cls._create_table(cur)

    @staticmethod
    def _insert(cur: Cursor, name: str) -> int:
        cur.execute(Item._query.insert, (name,))
        return cur.lastrowid

    @staticmethod
    def _update(cur: Cursor, item_id: int, name: str) -> int:
        return cur.execute(Item._query.update, (name, item_id))

    def save(self, cur: Cursor):
        if self.item_id is None:
            self.item_id = self._insert(cur, self.name)
        else:
            self._update(cur, self.item_id, self.name)
