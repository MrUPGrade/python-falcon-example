import click

from pft.config import DBConfig
from pft.app_context import ApplicationContextFactory
from pft.models import ModelBase


def app_context():
    db_config = DBConfig.from_env()
    acf = ApplicationContextFactory(db_config)
    return acf()


@click.group()
def cli():
    pass


@click.command()
def initdb():
    context = app_context()
    ModelBase.metadata.create_all(context.db.bind)


cli.add_command(initdb)

if __name__ == '__main__':
    cli()
