from contextlib import closing
from MySQLdb.connections import Connection

import click

from libs.db.mysql import connect, get_cursor
from models import Item

@click.group('items')
@click.pass_context
def app(ctx: click.Context = None):
    ctx.obj = ctx.with_resource(closing(connect()))

pass_conn = click.make_pass_decorator(Connection)


@app.command()
@click.option('--drop', is_flag=True, default=False)
@pass_conn
def init(conn: Connection, drop: bool):
    """Init database."""
    with closing(get_cursor(conn)) as cur:
        Item.init(cur, drop)


@app.command()
@click.argument('name')
@pass_conn
def create(conn: Connection, name: str):
    """Create item."""
    with closing(get_cursor(conn)) as cur:
        item = Item(name=name)
        item.save(cur)
    conn.commit()


if __name__ == '__main__':
    app()
