from contextlib import closing
from libs.db.mysql import connect, get_cursor

with closing(connect()) as conn:
    with closing(get_cursor(conn)) as cur:
        cur.execute("""
        CREATE TABLE test (
            id INT(11) NOT NULL AUTO_INCREMENT,
            PRIMARY KEY (id)
        )
        """)
