#!/usr/bin/env python3


from cgi import parse_qs, escape


def app(env, start_response):
    params = parse_qs(env['QUERY_STRING'])
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return ('{key}={val}'.format(key=k, val=v) for k, v in params.items())
