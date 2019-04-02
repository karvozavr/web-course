#!/usr/bin/env python3


from cgi import parse_qs, escape


def app(env, start_response):
    params = env['QUERY_STRING'].split('&')
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return map(lambda x: (x.strip() + '\n').encode(), params)
