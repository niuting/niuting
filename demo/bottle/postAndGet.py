#!/usr/bin/env python
# encoding: utf-8

from bottle import get, post, request, run

@get('/login')
def login():
    return '''
            <form action = "/login" method = "post">
                Username: <input name = "username" type = "text" />
                Password: <input name = "password" type = "password" />
                <input value = "Login" type = "submit" />
            </form>

        '''

@post('/login')
def do_login():
    username = request.forms.get('username')
    userpassord = request.forms.get('password')
    if username == '123' and userpassord == '234':
        return "<p> Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>p>"

if __name__ == "__main__":
    run(host = "172.17.6.223", port = 8080)

