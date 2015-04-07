#!/usr/bin/env python
# encoding: utf-8

from bottle import *
@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root = './')#可以从浏览器下载本地文件

if __name__ == "__main__":
    run(host = "172.17.6.223", port = 8080)


#执行curl： curl 172.17.6.223:8080/static/postAndGet.py
