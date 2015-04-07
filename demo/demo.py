#!/usr/bin/env python
# encoding: utf-8

import bottle
from bottle import post, request, get


@post("/api")
def post_file():
    '''
    try:

        # rJson = request.json  ## body
        print 'post**********************'
    except ValueError:
        return {
             "ok": False
        }

#   filename, context = rJson.get('filename'), rJson.get('context')
#   open(filename).write(context)

    return {'ok': True}
    '''
    return "hehe"

@get("/api/<filename>")   ## URL
def get_file(filename):
    print "get******************************"
    return {
        "context": open(filename).read()
    }


@get("/niuting/<arg>")
def niuting(arg):
    print "niuting*****************"
    return arg


if __name__ == "__main__":
    bottle.run(host='172.17.6.223', port = 8080)

'''
rJson = ""

@post("/api")
def post_file():
    try:
        global rJson
        rJson = request.json
        print rJson
    except ValueError:
        return {
                    "ok" : False
                    }
        return {'ok' : True}
@get("/api/<filename>")
def get_file(filename):
    global rJson

    print "****************"

    return rJson
    _

if __name__ == "__main__":
    bottle.run(host = '172.17.6.223', port = 8080)
'''
