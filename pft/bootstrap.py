import falcon

from pft.config import DBConfig
from pft.middleware import CustomAuth
from pft.resources.status import register as status_register
from pft.resources.notes import register as notes_register
from pft.resources.proxy import register as proxy_register
from pft.app_context import ApplicationContextFactory


def create_falcon_app():
    db_config = DBConfig.from_env()
    falcon.request.Request.context_type = ApplicationContextFactory(db_config)

    middlewares = [
        # CustomAuth(),
    ]

    app = falcon.API(middleware=middlewares)
    status_register(app, "/status")
    notes_register(app)
    proxy_register(app)

    return app
