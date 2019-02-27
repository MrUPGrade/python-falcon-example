from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from pft.config import DBConfig


def sqlalchemy_session_maker(db_config: DBConfig):
    engine = create_engine(db_config.to_sqlalchemy(), echo=db_config.echo)
    return sessionmaker(bind=engine)


class ApplicationContext:
    def __init__(self, db_session_maker):
        self._db_session_maker = db_session_maker
        self._db_session = None

    @property
    def db(self):
        if not self._db_session:
            self._db_session = self._db_session_maker()

        return self._db_session


class ApplicationContextFactory:
    def __init__(self, db_config: DBConfig):
        self._db_config = db_config
        self._db_session_maker = sqlalchemy_session_maker(self._db_config)

    def __call__(self, *args, **kwargs):
        return ApplicationContext(self._db_session_maker)
