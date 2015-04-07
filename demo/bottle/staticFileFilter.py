#!/usr/bin/env python
# encoding: utf-8
from bottle import error
from route import *
@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root = './static/')

@error(404)
def error404(error):
    print "****************"
    return "Sorry, Nothing here"

if __name__ == "__main__":
    run(host = "172.17.6.223", port = 8080)
