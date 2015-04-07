#!/usr/bin/env python
# encoding: utf-8

from bottle import *

@route('/restricted')
def restricted():
    abort(404, "Sorry, can't find file")

if __name__ == "__main__":
    run(host = '172.17.6.223', port = 8080)

