#!/usr/bin/env python
# encoding: utf-8

from bottle import *

@route('/images/<filename:re:.*.py>')
def send_image(filename):
    return static_file(filename, root = './', mimetype = 'image/py')

@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root = './')

if __name__ == "__main__":
    run(host = '172.17.6.223', port = 8080)
