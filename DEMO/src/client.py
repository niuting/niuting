#!/usr/bin/env python
# encoding: utf-8

import urllib2
import urllib
import sys
import logging

from config_logger import LogConfig
from path import InitPath

def create_file(dirname, filename):
    '''Create a file specified path'''

    path = InitPath(dirname, filename)
    path.show_path()

    return path.get_path()


def init_log():
    '''Configuration log file'''

    path = create_file('log/', 'client.log')
    if(path):
        log = LogConfig(path)
        log.config_log()

        return log
    else:
        logging.error('该路径不存在')
        sys.exit(1)


def http_post(url, line):
    '''Request to the server sends the page'''

    log = init_log()
    try:
        req = urllib2.Request(url, line)
        req.add_header('Content-Type', 'text/plain')
        req.add_header('Content-Encoding', 'utf-8')
        repose = urllib2.urlopen(req)

        return repose.read()
    except urllib2.URLError:
        log.logger().error('Urllib2 生成页面请求数据异常')
        print '_________________'
        sys.exit(1)


def create_table():
    '''Create a table'''

    log = init_log()
    file = create_file('lib/', 'userinfo.data')
    url1 = 'http://172.17.6.223:8080/api/first'
    url2 = 'http://172.17.6.223:8080/api'
    i = 0           #用于区分首行和其他行
    try:
        fp = open(file)
        for line in fp.readlines():
            if(i == 0):
                url = url1
            else:
                url = url2

            sqlname = http_post(url, line.strip('\n'))
            print "sqlname = ", sqlname
            i += 1
    except IOError:
        log.logger().error('要打开的文件名不存在')
    finally:
        fp.close()


def deal_argv():
    '''Process command-line arguments'''

    log = init_log()
    argv = ""
    i = 0           #过滤掉命令本身
    try:
        for eacharg in enumerate(sys.argv):
            if(i == 0):
                pass
            else:
                argv = argv + eacharg[1] + " "
            i += 1
        print 'argv = ', argv.strip()
        return argv
    except TypeError:
        log.logger().error('传递的参数有误')
        sys.exit(1)



def insert_data():
    '''Add a data to the database'''

    url = 'http://172.17.6.223:8080/api/insert'
    argv = deal_argv()
    sqlname = http_post(url, argv.strip())
    print "sqlname = ", sqlname


def search_data():
    '''Search a data from table'''

    url = 'http://172.17.6.223:8080/api/search'
    argv = deal_argv()
    print type(argv)
    print argv.lstrip()
    sqlname = http_post(url, argv.strip())
    print "sqlname = ", sqlname


#create_table()
#insert_data()
search_data()



