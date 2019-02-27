import base64
import binascii
import os

import falcon


class Health:
    def on_get(self, req, resp):
        quote = {
            'status': 'healthy'
        }

        resp.media = quote


class DBConn:
    def on_get(self, req, resp):
        req.context.db.connection().execute('select 1')

        quote = {
            'status': 'healthy'
        }

        resp.media = quote


class Env:
    def on_get(self, req, resp):
        auth = req.auth

        try:
            if not auth or not auth.startswith('Basic '):
                raise falcon.HTTPUnauthorized()

            dec = base64.b64decode(auth.replace('Basic ', '')).decode('ascii')
            secret = os.getenv("PFT_ADMIN_SECRET")

            if not secret:
                raise falcon.HTTPUnauthorized()

            if not dec == f'admin:{secret}':
                raise falcon.HTTPUnauthorized()

        except binascii.Error:
            raise falcon.HTTPUnauthorized()

        result = {}
        for k, v in os.environ.items():
            result[k] = v

        resp.media = result


def register(app: falcon.API, sub_path=''):
    app.add_route(sub_path + '/health', Health())
    app.add_route(sub_path + '/db', DBConn())
    app.add_route(sub_path + '/env', Env())
