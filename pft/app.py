from pft.bootstrap import create_falcon_app

app = create_falcon_app()

if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
