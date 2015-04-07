#!/usr/bin/env python
# encoding: utf-8

from bottle import *
from bottle import response, request
import io
import json
import os
import subprocess
import sys

rJson = ""

def returnNum(str):
    if str == "true" or str == "True":
        return {'ok': True}
    elif str == 'false' or str == 'False':
        return {'ok': 'False'}
    else:
        print "Error Number"


def write_file_os(filename, context, option):
    if os.path.exists("./filename"):
        os.system("rm %s" %filename)#判断文件是否存在，若存在则删除

    os.system("touch %s" %filename)


def write_file_sub(filename, context, option):
    if os.path.exists("./filename"):
        subprocess.Popen("rm %s" %filename, shell = True)#shell为真的话 unix下相当于args前面添加了 "/bin/sh“ ”-c”>

    subprocess.Popen("touch %s" %filename, shell = True)#必须为无缓冲，否则写不进文件>


def write_file(filename, context, option):#参数1：   要写入文件的内容 参数2：写入的方式
    write_file_sub(filename, context, option)
    #write_file_os(filename, context, option)
    try:
        print "write: filename = %s" %filename
        f = open(filename, option, 1024)
        Str = json.dumps(context)
        Str1 = str(Str)
        f.write(Str1)   #去除关闭文件，统一在finally中关闭
    except IOError, Environment:
        returnNum("False")
    finally:
        try:
            f.close()
        except IOError:
            print "can't close file"
            os.exit(1)


@post('/api')
def post_file():
    try:
        global rJson
        request.accept="application/json"
        try:
            rJson = request.json
        except ValueError:
            print "Error : ValueError"

        filename = rJson.get('filename')
        context = rJson.get('content')

        write_file(filename, context, 'w+')

        print "filename : %s" %(json.dumps(filename))
        print "context : %s" %(json.dumps(context))

    except ValueError:
        returnNum('False')
    returnNum('True')


@get('/api/<filename>')
def post_file(filename):
    try:
        context = open(filename).read()

        data = {'filename': filename, 'content': context}
        rJson = json.dumps(data)

        return rJson

    except IOError:
        returnNum("False")


@get('/api/json')
def post_str():
    try:

        return rJson

    except ValueError:
        returnNum('False')


if __name__ == "__main__":
    run(host = '172.17.6.223', port = 8080)
