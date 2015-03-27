#!/usr/bin/env python
# encoding: utf-8

import os

#OS模块

print os.name;#字符串指示你正在使用的平台,比如对于Windows，它是'nt'，而对于Linux/Unix用户，它是'posix'。
print os.getcwd();#函数得到当前工作目录，即当前Python脚本工作的目录路径。
print os.getenv('python');#函数分别用来读取和设置环境变量 os.putenv()
print os.listdir("../../");#返回指定目录下的所有文件和目录名。
#os.remove('pickle.pyc');#函数用来删除一个文件
os.system("ls -a");#函数用来运行shell命令
print os.linesep;#字符串给出当前平台使用的行终止符。例如，Windows使用'\r\n'，Linux使用'\n'而Mac使用'\r'

print os.path.split('os.getcwd()');#函数返回一个路径的目录名和文件名


