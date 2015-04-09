#!/usr/bin/env python
# encoding: utf-8

#demo1.py

from bottle import get, post, run, request
import json
import os
import logging

PATH = "/home/zhangbo/niuting/PYTHON/demo/Data"
RJSON = ""

LOG_FILENAME = './LOG/log_demo.txt'
logging.basicConfig(filename=LOG_FILENAME, filemode ='w', level=logging.DEBUG) #配置logging
logging.info("this is the demoy1's log")   ##debug中的内容将被输出

def get_cwd():
    "检查是否存在该目录，不存在则创建"
    logger = logging.getLogger("get_cwd")
    try:
        if not os.path.isdir(PATH):
            os.mkdir(PATH)

        os.chdir(PATH)
        return_num('True')
    except OSError:
        logger.debug("get_cwd: OSError")
        return_num('False')


def return_num(value):
    "定义返回值函数"
    if value.lower() == 'true' or value.lower() == 'false':
        return {'ok' : value.capitalize()}


def write_file(filename, context, option):#参数1：   要写入文件的内容 参数2：写入的方式
    "将用户传入的json数据中的数据内容写入以json数据中的文件名命名的文件"
    logger = logging.getLogger("write_file")
    try:
        logger.info("filename = %s" %filename)

        path = PATH + "/" + filename
        logger.info("path = %s" %path)

        filepoint = open(path, option, 1024)
        logger.info("context = %s" %context)

        strdata = json.dumps(context, ensure_ascii=False).encode('utf-8')   #p43

        logger.info("strdata = %s" %strdata)

        filepoint.write(strdata)   #统一在finally中关闭

        return_num('True')
    except IOError:
        return_num("False")
    finally:    #finally语句会在return前执行
        try:
            filepoint.close()
        except IOError:
            logger.debug("can't close file")
            return_num('False')


@post('/api')
def post_str():
    "接收处理用户传入的json数据"
    logger = logging.getLogger("post_file")
    try:
        request.accept = "application/json"
        try:
            global RJSON
            RJSON = request.json
            logger.info("RJSON = %s" %RJSON)
        except ValueError:
            logger.info("Error : ValueError")

        logger.info("type(RJSON) = %s" %type(RJSON))

        filename = RJSON.get('filename')
        context = RJSON.get('content')

        if get_cwd():
            write_file(filename, context, 'w+') #将用户数据写入文件"w+"如果文件已存在则将其覆盖，不存在则重新创建
        else:
            return_num('False')

        print "filename : %s" %(json.dumps(filename))
        print "context : %s" %(json.dumps(context, ensure_ascii=False))

    except ValueError:
        return return_num('False')
    return return_num('True')


@get('/api/<filename>')
def get_file(filename):
    "从<filename>文件中获取数据，并返回给用户"
    logger = logging.getLogger("get_file")
    try:
        context = open(filename).read()
        print "post_file: context %s" %context
        logger.info("context = %s" %context)

        data = {'filename': filename, 'content': context}
        data1 = json.dumps(data, ensure_ascii=False)
        logger.info("get_file: data1 = %s" %data1)

        return data1

    except IOError:
        return return_num("False")


@get('/api/json')
def get_str():
    "将json数据返回给用户"
    try:
        global RJSON
        return RJSON
    except ValueError:
        return return_num('False')


if __name__ == "__main__":
    run(host='172.17.6.223', port=8080)
