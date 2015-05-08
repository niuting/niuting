#!/usr/bin/env python
# encoding: utf-8

import sys
import logging
from bottle import get, post, run, request
import sqlalchemy.orm as sqlo
import sqlalchemy.ext.declarative as sqle

from config_logger import LogConfig
from path import InitPath
from userclass import UserSql

def write_table(datalist):
    '''Create table'''

    db = UserSql()
    user_db = UserSql._UserTable(int(datalist[0]), datalist[1], int(datalist[2]))
    session = db.get_session()
    session.add(user_db)
    session.commit()
    tablename = user_db.get_table_name()
    return tablename


def search_table(key, value):
    '''Search table'''

    db = UserSql()
    session = db.get_session()
    print '\\', key, value
    print '\\', key.lower().strip()
    if (key.lower() == 'id'):
        value = int(value)
        alldata = session.query(UserSql._UserTable).filter(UserSql._UserTable.id == value).scalar()
    elif (key.lower().strip() == 'name'):
        alldata = session.query(UserSql._UserTable).filter(UserSql._UserTable.name == value).scalar()
    elif(key.lower() == 'age'):
        alldata = session.query(UserSql._UserTable).filter(UserSql._UserTable.age == value).scalar()
    else:
        print "数据库中没有该字段"
    print "***********************"
    print alldata.id, alldata.name, alldata.age
    '''
    for somedata in alldata:
        print somedata.id
    '''


def splite_data(data, separator):
    '''The string types of form data into the list'''

    typelist =[]
    datalist = []
    i = 0
    strlist = data.split(separator)
    for st in strlist:              #将字段名称和字段类型分别存储在两个列表中
        if(i%2):
            print 'ty : ', st
            typelist.append(st)
        else:
            print 'da : ', st
            datalist.append(st)
        i += 1

    return (datalist, typelist)


def create_file(dirname, filename):
    '''Create a file specified path'''

    path = InitPath(dirname, filename)
    path.show_path()

    return path.get_path()


def init_log():
    '''Configuration log file'''

    path = create_file('log/', 'server.log')
    if(path):
        log = LogConfig(path)
        log.config_log()

        return log
    else:
        logging.error('该路径不存在')
        sys.exit(1)




@post('/api/first')
def post_file_fild():
    '''Deal with first line fild name'''

    log = init_log()          #初始化日志
    request.accept = 'text/plain'
    data = request.body.read()
    if(len(data)):
        for i in ('(',')','  '):
            data = data.replace(i, ' ')             #将字段中其他分隔符都用‘ ’替换
        datalist, typelist = splite_data(data.strip(), ' ')
        log.logger().debug('datalist: %s, typelist: %s'
                                    %(datalist, typelist))
        #tablename = write_table(datalist, typelist)       #创建数据库，并将数据库名称返回
        '''
        if(tablename):
            return tablename
        else:
            return None
        '''
    else:
        log.logger().error('用户发送的数据为空')
        return None


@post('/api')
def post_file_content():
    print request.get_header('Content-Type')
    request.accept = 'text/plain'

    data = request.body.read()
    print data
    datalist = data.split(' ')
    tablename = write_table(datalist)
    print 'type(data) = ',type(datalist), tablename
    return tablename

@post('/api/insert')
def insert():
    '''Add a record to the database'''

    request.accept = 'text/plain'
    data = request.body.read()
    print "************************"
    print type(data)
    print data
    datalist = data.split(' ')
    print datalist
    tablename = write_table(datalist)
    return tablename


@post('/api/search')
def search():
    '''Search a record in the table'''

    request.accept = 'text/plain'
    data = request.body.read()
    print 'data = ', data

    search_table('name', 'niu')


if __name__ == '__main__':
    run(host='172.17.6.223', port=8080)

