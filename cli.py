#!/usr/local/bin/python
"""Command line interface"""
import click
from MySQLdb.connections import Connection

from application import app
from application import pass_conn
from models import DB
from models import Item


@app.command()
@pass_conn
def init(conn: Connection):
    """Init database."""
    DB.init(conn)


@app.command()
@click.argument("name")
@pass_conn
def create(conn: Connection, name: str):
    """Create item."""
    item = Item(name=name)
    item.save(conn)
    conn.commit()


if __name__ == "__main__":
    app()
