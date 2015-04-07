#!/usr/bin/env python
# encoding: utf-8

# File http_post.py

from bottle import *
import urllib
import urllib2
import json

def urlError():
    print "+++urlopen error: Connection refused"

def http_post():
    try:
        url='http://172.17.6.223:8080/api'
    except URLError:
        urlError()

    filename ={"filename":"dic.txt", "content":["one", "two", "three"]}     #数据内容
    jdata = json.dumps(filename)        # 对数据进行JSON格式化编码
    print type(jdata)#显示jdata类型
    req = urllib2.Request(url, jdata)       # 生成页面请求的完整数据
    req.add_header('Content-Type', 'application/json')
    #print type(req)

    response = urllib2.urlopen(req)       # 发送页面请求
    return response.read()                    # 获取服务器返回的页面信息


def http_get_json():
    try:
        url='http://172.17.6.223:8080/api/json'
    except URLError:
        urlError()
    req = urllib2.Request(url)
    req.add_header('Content-Type', 'application/json')
    response = urllib2.urlopen(req)

    data = response.read()

    print "type(data) : %s" %(type(data))
    print "data = %s" %(data)

    rJson = json.loads(data)        #将json数据解包
    for key in rJson:
        if key == "filename":       #用key值匹配内容
            print "filename : %s" % rJson[key]
        elif key == "content":
            print "content : %s" % rJson[key]
        else:
            pass
def http_get_file():
    try:
        url='http://172.17.6.223:8080/api/usr_info.txt'
    except URLError:
        urlError()
    req = urllib2.Request(url)
    req.add_header('Content-Type', 'application/json')
    response = urllib2.urlopen(req)

    data = response.read()

    print "data : %s" % data

resp = http_post()
print resp

print http_get_json()
print "_______________________________"
print http_get_file()

