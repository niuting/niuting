#!/usr/bin/env python
# encoding: utf-8

from bottle import route, run, template
@route('/')
@route('/hello/<name>')
def greet(name = 'Stranger'):
    return template('Hello {{name}}, how are you?', name = name)#使用模板

if __name__ == "__main__":
    run(host = '172.17.6.223', port = 6556)
