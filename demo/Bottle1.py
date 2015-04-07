#!/usr/bin/env python
# encoding: utf-8

import json
import bottle
from bottle import get, post, request
#bottle.post()

def check_login(username, password):
    if username == '123' and password == '234':
        return True
    else:
        return False

@bottle.route('/login')
def login():
    print "************"
    return '''<form action = "/login", method = "post">
                Usernmae: <input name = "username" type = "text" />
                Password: <input name = "password" type = "password" />
                <input value = "Login" type = "submit">
                </form>

            '''
#    return jsonData()

@bottle.route('/login', method = 'POST')
def do_login():
#    jsonData()
    username = bottle.request.forms.get('username')
    password = request.forms.get('password')
    print username
    print password

    if check_login(username, password):
        return '<p> Your login information was correct.</p>' #+jsonData()
    else:
        return '<p>Login faild. </p>'
'''
def jsonData():
    data = [{'username':'123', 'password':'234'}]
    Jdata = json.dumps(data)

    return Jdata
'''

bottle.run(host = '0.0.0.0', port = 8080)


