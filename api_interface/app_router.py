# -*- coding: utf-8 -*-

def application(env, start_response):
    doc_root = '/photo_log'
    path = env['PATH_INFO']
    if path == doc_root + '/':
        start_response('200 OK', [('Content-type', 'text/plain')])
        return [b'Hello World']
    elif path == doc_root + '/foo':
        start_response('200 OK', [('Content-type', 'text/plain')])
        return [b'foo']
    else:
        start_response('404 Not Found', [('Content-type', 'text/plain')])
        return [b'404 Not Found']
