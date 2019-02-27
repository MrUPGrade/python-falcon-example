import os

from dataclasses import dataclass, field


class ConfigError(Exception):
    def __init__(self, field):
        super().__init__('Missing environment variable %s' % field)


def get_env_var(name: str, prefix='', allow_empty=False):
    if prefix:
        env = prefix + '_' + name
    else:
        env = name

    value = os.getenv(env)
    if not allow_empty and not value:
        raise ConfigError(env)

    return value


@dataclass(init=True)
class DBConfig:
    name: str
    user: str
    password: str
    host: str
    port: int
    echo: bool = field(default=False)

    @classmethod
    def from_env(cls):
        name = get_env_var('DB_NAME', 'PFT')
        user = get_env_var('DB_USER', 'PFT')
        password = get_env_var('DB_PASS', 'PFT')
        host = get_env_var('DB_HOST', 'PFT')
        port = int(get_env_var('DB_PORT', 'PFT'))
        echo = bool(get_env_var('DB_ECHO', 'PFT', allow_empty=True))

        return cls(name=name, user=user, password=password, host=host, port=port, echo=echo)

    def to_sqlalchemy(self) -> str:
        return f'postgresql+psycopg2://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}'


