import datetime
from flask import json


def application(env, start_resp):
    headers = [('Content-Type', 'application/json')]
    start_resp('200 OK', headers)
    uri = env['wsgi.url_scheme'] + '://' + env['HTTP_HOST'] + env['RAW_URI']
    resp = json.dumps({'time': '{}'.format(datetime.datetime.now()), 'url': '{}'.format(uri)})
    return [resp.encode('utf-8')]

