"""Application context"""
from contextlib import closing

import click
from MySQLdb.connections import Connection

from libs.db.mysql import connect


@click.group("items")
@click.pass_context
def app(ctx: click.Context = None) -> None:
    """App"""
    if ctx is not None:
        ctx.obj = ctx.with_resource(closing(connect()))


pass_conn = click.make_pass_decorator(Connection)
