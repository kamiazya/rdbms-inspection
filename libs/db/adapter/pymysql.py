# Copy and Edit from
# https://github.com/kajuberdut/aiosql-mysql/blob/main/aiosql_mysql/adapters/pymysql.py
import re
from contextlib import contextmanager

# looking for : without a \ escaping it
# followed by any number of letters, numbers or "_", "-"" characters.
variables = re.compile(r"""[^\\](:[\w\d_-]*)""")


class PyMySQLAdaptor:
    @staticmethod
    def process_sql(_query_name, _op_type, sql):
        return variables.sub(
            lambda m: f"{m.group(0)[:1]}%({m.group(1)[1:]})s", sql
        )

    @staticmethod
    def select(conn, _query_name, sql, parameters, record_class=None):
        with conn.cursor() as cur:
            cur.execute(sql, parameters)
            results = cur.fetchall()
            if record_class is not None:
                column_names = [c.name for c in cur.description]
                results = [
                    record_class(**dict(zip(column_names, row)))
                    for row in results
                ]
        return results

    @staticmethod
    def select_one(conn, _query_name, sql, parameters, record_class=None):
        with conn.cursor() as cur:
            cur.execute(sql, parameters)
            result = cur.fetchone()
            if result is not None and record_class is not None:
                column_names = [c.name for c in cur.description]
                result = record_class(**dict(zip(column_names, result)))
        return result

    @staticmethod
    def select_value(conn, _query_name, sql, parameters):
        with conn.cursor() as cur:
            cur.execute(sql, parameters)
            result = cur.fetchone()
        return result[0] if result else None

    @staticmethod
    @contextmanager
    def select_cursor(conn, _query_name, sql, parameters):
        with conn.cursor() as cur:
            cur.execute(sql, parameters)
            yield cur

    @staticmethod
    def insert_returning(conn, _query_name, sql, parameters):
        with conn.cursor() as cur:
            cur.execute(sql, parameters)
            # Edited
            return cur.lastrowid

    @staticmethod
    def insert_update_delete(conn, _query_name, sql, parameters):
        with conn.cursor() as cur:
            cur.execute(sql, parameters)

    @staticmethod
    def insert_update_delete_many(conn, _query_name, sql, parameters):
        with conn.cursor() as cur:
            cur.executemany(sql, parameters)

    @staticmethod
    def execute_script(conn, sql):
        with conn.cursor() as cur:
            cur.execute(sql)
