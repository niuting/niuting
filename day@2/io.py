#!/usr/bin/env python
# encoding: utf-8

import os

#输入
'''
#1. raw_input
str = raw_input("please input some you want to write: ");
print "receive input :", str;

#2. input//input([prompt]) 函数和raw_input([prompt]) 函数基本可以互换，但是input会假设你的输入是一个有效的Python表达式，并返回运算结果。 ]]
str = input("please input some you want to write: ");
print "receive input :", str;
'''

#打开和关闭文件和读写文件
'''
file1 = open("./tmp.c", "a+", 1024);
print "name of file :", file1.name;
print "closed or not: ", file1.closed;
print "model of file1: ", file.mode;

str = file1.read(1024);
print "file1:\n", str;

file1.close();

file1 = open("./tmp.c", "a+", 1024);
file1.write("hello world\n");
file1.close();

file1 = open("./tmp.c", "a+", 1024);
str = file1.read(1024);
print "file1:\n", str;

file1.close();
print "closed or not: ", file1.closed;
'''

#文件重命名
'''
os.rename("tmp.c", "tmp.txt");
'''

#删除文件
'''
os.remove("./tmp.txt");

'''
#显示当前路径
os.getcwd();


