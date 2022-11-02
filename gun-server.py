import json
""" from wsgiref.simple_server import make_server """

def application(environ, start_response):
    headers = [('Content-type', 'text/html')]
    start_response('200 OK ', headers)

    response = {
        "Identificador" :  "001"
    }

    return [bytes(json.dumps(response), 'utf-8')]


""" server = make_server('localhost', 8000, application)
server.serve_forever """