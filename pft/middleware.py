import falcon


class CustomAuth:
    def process_request(self, req, resp):
        auth = req.headers.get('MYAUTH', None)

        if auth != 'secret':
            raise falcon.HTTPUnauthorized()
