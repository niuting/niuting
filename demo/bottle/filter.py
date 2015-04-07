#!/usr/bin/env python
# encoding: utf-8

from bottle import route, run, static_file

@route('/object/<id:int>')
def callback(id):
    assert isinstance(id, int)

@route('/show/<name:re:[a-z]+>')
def callback(name):
    assert name.isalpha()
@route('/static/<path:path>')
def callback(path):
    return static_file(path)


if __name__ == "__main__":
    run(host = '172.17.6.223', port = 6556)
