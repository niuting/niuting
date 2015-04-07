#!/usr/bin/env python
# encoding: utf-8

from bottle import *

@route('/wiki/<page>')
def wiki(page):
    response.set_header('Content-Language', 'English')
    response.add_header('File-Language', 'Chinese')
    return response.get_header('File-Language')

if __name__ == "__main__":
    run(host = '172.17.6.223', port = 8080)
