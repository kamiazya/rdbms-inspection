#!/usr/local/bin/python
"""Command line interface"""
from contextlib import closing

import click
from MySQLdb.connections import Connection

from application import app
from application import pass_conn
from libs.db.mysql import get_cursor
from models import Item


@app.command()
@click.option("--drop", is_flag=True, default=False)
@pass_conn
def init(conn: Connection, drop: bool):
    """Init database."""
    with closing(get_cursor(conn)) as cur:
        Item.init(cur, drop)


@app.command()
@click.argument("name")
@pass_conn
def create(conn: Connection, name: str):
    """Create item."""
    with closing(get_cursor(conn)) as cur:
        item = Item(name=name)
        item.save(cur)
    conn.commit()


if __name__ == "__main__":
    app()
