import falcon
import requests


def sink(req, resp):
    if req.method != 'GET':
        raise falcon.HTTPBadRequest()

    url = 'https://jsonplaceholder.typicode.com/' + req.relative_uri[7:]
    proxy_resp = requests.get(url)
    if proxy_resp.status_code != 200:
        raise falcon.HTTPBadRequest('something wrong ;)')

    resp.media = proxy_resp.json()


def register(app: falcon.API, sub_path=''):
    app.add_sink(sink, sub_path + '/proxy')
