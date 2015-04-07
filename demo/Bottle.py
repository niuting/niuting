#!/usr/bin/env python
# encoding: utf-8

'''
import bottle

@bottle.route('/hello')
def hello():
    return "hello world"

bottle.run(host = "localhost", port = 8080, debug = True)
'''

from bottle import *
import json

'''
#打开浏览器，输入：http://172.16.160.122:8080/helloworld/BigData，你只要将ip地址改成你自己的地址就行了
@route('/helloworld/hehe/:yourwords', methods=['GET', 'POST'])

def hello(yourwords):
    return 'hello world '+ yourwords

run(host = 'localhost', port = 8080)#run()函数用来启动Bottle内置的Web服务器.Web服务器会监听地址0.0.0.0的8080端口
'''

#多路径：route()函数是一个decorator，并且通过URL地址来指向一个回调函数

'''
@route('/')
@route('/hello/<name>')
def hello(name = 'Stranger'):
    return 'hello %s' % name

run(host = '0.0.0.0', port = 8080)
'''
#通配符
'''
@route('/hello/<id:int>')
@route('/show/<name:re:[a-z]+>>')
@route('/static/path:path')

def callback(id):
    assert isinstance(id, int)
'''

@route('/show/<name:re:[a-z]+>')

def callback(name):
    assert name.isalpha()
    Jdata = jsonData()
    return 'hello ' + Jdata

def jsonData():
    data = [{'one' : 1, 'two':2, 'three':3}]
    Jdata = json.dumps(data)
    return Jdata

'''
@route('/static/path:path')

def callback(path):
    return path
'''

run(host = '0.0.0.0', port = 8080)
#run(host = '192.0.0.0', port = 8080)




