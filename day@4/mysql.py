#!/usr/bin/env python
# encoding: utf-8

import MySQLdb as MS    #引入MySQLdb模块


def printMass(str):
    print str

db = MS.connect(host='127.0.0.1', user='root',passwd='zhangbo');    #连接到数据库
if db:
    print "链接数据库成功"
else:
    print "链接数据库失败"

#创建游标
cur = db.cursor();
if cur:
    printMass("创建游标成功")
else:
    printMass("创建游标失败")

#删除原有数据库
if cur.execute("drop database if exists niuting"):
    printMass("删除原有数据库成功")
else:
    printMass("删除原有数据库失败")

#创建数据库
if cur.execute("create database  if not exists niuting"):
    printMass ("创建数据库成功")
else:
    printMass ("创建数据库失败")
#cur.execute("create database if not exists python")

#显示数据库
cur.execute("show databases")

#选择数据库
db.select_db('niuting')

'''
if db.select_db('niuting'):
    printMass ("选择数据库成功")
else:

    printMass ("选择数据库失败")
'''
'''
#删除与数据表
if cur.execute("drop table if exists student"):
    printMass("删除原有数据表成功")
else:
    printMass("删除原有数据表失败")
'''
#创建数据表
cur.execute("create table student(id int ,name varchar(20),class varchar(30),age varchar(10))")
'''
if cur.execute("create table student(id int ,name varchar(20),class varchar(30),age varchar(10))"):
    printMass("创建表成功")
else:
    printMass("创建表失败")
'''
#插入一条数据
cur.execute("insert into student(id, name, class, age) values (4, 'ningqi', '1101', 2)")
cur.execute("insert into student(id, name, class, age) values (3, 'niuting', '1101', 3)")

#查看数据表

print "更新前的数据"
cur.execute("select * from student")

#print "*************************************"

#更新一条数据
cur.execute("update student set class = '1102', age = 10 where name = 'ningqi'")

#查看更新后的数据表

print "更新后的数据"

cur.execute("select * from student")

#print cur.execute("SELECT VERSION()")

#删除一条数据
cur.execute("delete from student where class = '1102' and age = 10")

#查看删除数据后的数据表
cur.execute("select * from student")

#从数据库中获取数
data = cur.fetchall()
if data:
    print data
else:
    print "获取数据库中的数据失败"

#显示数据库
print "显示数据库"
cur.execute("show databases")

#显示当前时间
cur.execute("select now()")

#重命名数据表
cur.execute("rename table student to studentInfo")

#查看数据库中得所有表
cur.execute("show tables")

#关闭cur对象
cur.close()
db.close()

'''
if cur.close():
    print "成功关闭cur游标"
else:
    print "关闭cur游标出错"
#关闭db对象，断开连接
if db.close():
    print "成功关闭数据库"
else:
    print "关闭数据库出错"
'''
