# -*- coding: utf-8 -*-

import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')
from app.interface.folder import GetUserAllFolder

def application(env, start_response):
    doc_root = '/photo_log'
    path = env['PATH_INFO']
    if path == doc_root + '/':
        start_response('200 OK', [('Content-type', 'text/plain')])
        data = GetUserAllFolder(1)
        json = data.get_json()
        return json.encode("UTF-8")
    elif path == doc_root + '/foo':
        start_response('200 OK', [('Content-type', 'text/plain')])
        return [b'foo']
    else:
        start_response('404 Not Found', [('Content-type', 'text/plain')])
        return [b'404 Not Found']
