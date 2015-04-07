#!/usr/bin/env python
# encoding: utf-8

from bottle import *
from bottle import response, request
import io
import json
import requests
import os

data = ""
rJson = ""

def write_file(fStr, option):#参数1：   要写入文件的内容 参数2：写入的方式
    if os.path.exists("./usr_info.txt"):    #判断文件是否存在，若存在则删除
        os.system("rm usr_info.txt")

    os.system("touch ./usr_info.txt")
    try:
        f = open("./usr_info.txt", option, 1024)
        f.write(fStr)
        f.close()

        return {'ok' : True}

    except IOError:
        return {'ok' : False}

    finally:
        f.close()

@post('/api')
def post_file():
    try:
        global data
        global rJson
        request.accept="application/json"
        rJson = request.json

        print "type(rJson) : %s" %(type(rJson))

        filename = rJson.get('filename')
        context = rJson.get('content')


        print "file: %s" %type(filename)
        print "repr(rJson) %s" %rJson
        write_file(repr(rJson), 'w+')

        print "filename : %s" %(json.dumps(filename))
        print "contxt : %s" %(json.dumps(context))



    except ValueError:
        return {'ok': False}
    return{'ok': True}

@get('/api/<filename>')
def post_file(filename):
    try:
        data = open(filename).read()

        return data


    except IOError:
        return
@get('/api/json')
def post_str():
    try:
        global rJson

        return rJson

    except ValueError:
        return {'ok': False}

if __name__ == "__main__":
    run(host = '172.17.6.223', port = 8080)
