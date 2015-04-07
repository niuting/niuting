#!/usr/bin/env python
# encoding: utf-8

from bottle import *

@route('/download/<filename:path>')
def download(filename):
    return static_file(filename, root = "./", download = 'forceDownload.py')#在下载文件时，会将文件重命名为当前指定的文件名。浏览器验证

if __name__ == "__main__":
    run(host = '172.17.6.223', port = 8080)
