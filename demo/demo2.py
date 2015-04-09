#!/usr/bin/env python
# encoding: utf-8

# File http_post.py

import urllib2
import json
import logging

LOG_FILENAME = './LOG/log_demo2.txt'
logging.basicConfig(filename=LOG_FILENAME, filemode='w', level=logging.DEBUG)   #配置logging
logging.info("this is the demo2's log")   #info中的内容将被输出

def url_error():
    "定义URL错误"
    logging.debug("urlopen error: Connection refused")


def print_json_data(rjson):
    "从json数据中读取文件名和文件内容"
    for key in rjson:
        if key == "filename":   #用key值匹配内容
            print "filename : %s" % rjson[key]
        elif key == "content":
            print "content : %s" % rjson[key]
        else:
            pass


def http_post():
    "向服务器发送页面请求"
    try:
        url = 'http://172.17.6.223:8080/api'
    except urllib2.URLError:
        url_error()

    filename = {"filename":"dic.txt", "content":["one", "two", "三"]}   #数据内容
    jdata = json.dumps(filename, ensure_ascii=False)    #对数据进行JSON格式化编码

    req = urllib2.Request(url, jdata)   #生成页面请求的完整数据
    req.add_header('Content-Type', 'application/json')

    response = urllib2.urlopen(req) #发送页面请求
    return response.read()  #获取服务器返回的页面信息


def http_get_json():
    "从服务器获取用户所需json数据"
    try:
        url = 'http://172.17.6.223:8080/api/json'
    except urllib2.URLError:
        url_error()

    req = urllib2.Request(url)
    req.add_header('Content-Type', 'application/json')
    response = urllib2.urlopen(req)

    data = response.read()

    logging.info("type(data) : %s" %(type(data)))
    logging.info("data = %s" %(data))

    rjson = json.loads(data)        #将json数据解包
    filename = rjson.get('filename')
    content = rjson.get('content')
    context = json.dumps(content, ensure_ascii=False)

    print "filename : %s" %filename
    print "context : %s" %context


def http_get_file():
    "以指定的文件名从服务器获取用户所需json数据"
    try:
        url = 'http://172.17.6.223:8080/api/dic.txt'
    except urllib2.URLError:
        url_error()
    req = urllib2.Request(url)
    req.add_header('Content-Type', 'application/json')
    response = urllib2.urlopen(req)

    data = response.read()
    rjson = json.loads(data)
    print_json_data(rjson)


print "please input the number you choice!(1:post_json, 2:get_json, 3:get_file)"
NUMBER = raw_input()
if NUMBER == "1":
    DATA_INFO = http_post()
    print DATA_INFO
elif NUMBER == "2":
    RESP = http_post()
    print http_get_json()
elif NUMBER == "3":
    print http_get_file()
else:
    print "Wrong Number"

