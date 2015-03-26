#!/usr/bin/env python
# encoding: utf-8

import time
import calendar#获取某月日历

ticks = time.time()#函数time.time()用ticks计时单位返回从12:00am, January 1, 1970(epoch) 开始的记录的当前操作系统时间
print "Number of ticks since 12:00am, January 1, 1970: ", ticks
localtime = time.localtime(time.time())#获取当前时间
print "local time is ", localtime
localtime = time.asctime(time.localtime(time.time()))#获取格式化时间
print "local time is ", localtime


cal = calendar.month(2015, 3)
print "calendar is ", cal
cal = calendar.weekday(2015, 3, 4)
print "calendar is ", cal
