#!/usr/bin/env python
# encoding: utf-8

from bottle import route, request, run, post
import json

#@route('/upload')
@post('/upload')
def do_upload():
   return '''<form enctype = 'application/json'>
                <input type = 'file' name = 'file' value = usriNFO multiple>
               </form>
           ''' + do_upload1()
def do_upload1():
    return '''<form enctype = 'application/json'>
        <input name = 'usrname' value = 'ningqi'>
        <input name = 'age' value = 6>
        <input name = 'weight' value = 42>
        </form>
'''

'''
@post('/upload')
def upload():
    name = request.forms.get('name')
    return 'hello world {0}'.format(name)
'''
run(host = '0.0.0.0', port = 8080)



