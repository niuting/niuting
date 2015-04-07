#!/usr/bin/env python
# encoding: utf-8

from bottle import *

@route('/iso')
def get_iso():
    response.charset = 'ISO-8859-15'

    return u"This will be sent with ISO-8859-15 encoding."

@route('/latin9')
def get_latin():
    response.content_type = 'text/html; charset=latin9'
    return u'ISO-8859-15 is also know as latin9.'

if __name__ == "__main__":
    run(host = "172.17.6.223", port = 8080)
