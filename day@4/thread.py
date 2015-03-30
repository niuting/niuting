#!/usr/bin/env python
# encoding: utf-8

import thread
import threading
import time

'''
#为线程定义一个函数
def print_time(threadName, delay):
    count = 0
    while delay < 5 and count < 5:
        time.sleep(delay)
        count += 1
        print "%s: %s" % (threadName, time.ctime(time.time()))
        threading.enumerate()
    try:
        threading.enumerate()
        #threadName.stop()
        pass
    except:
        print "线程未能正确终止"

try:
    thread.start_new_thread(print_time, ("Thread_1", 4))
    thread.start_new_thread(print_time, ("Thread_2", 2))
     #thread.exit()
    threading.enumerate()
except:
    print "Error: unable to start thread"

while 1:
    pass
'''
#使用threading模块
'''
class myThread(threading.Thread):

    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print "Starting " + self.name
        print_time(self.name, self.counter, 5)
        print "Exitint " + self.name

def print_time(threadName, delay, counter):
    while counter:
        if counter == 1:
            thread.exit()
        time.sleep(delay)
        print "%s %s" % (threadName, time.ctime(time.time()))
        counter -= 1

#创建新线程
thread1 = myThread(1, 'Thread-1', 1)
thread2 = myThread(2, 'Thread_2', 2)

thread1.start()
thread2.start()

print "Exiting Main Thread"
'''
#线程同步

class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print "Starting " + self.name
        threadLock.acquire()
        #threading.Lock().acquire()
        print_time(self.name, self.counter, 5)
        #threading.Lock().release()
        threadLock.release()

def print_time(threadName, delay, counter):
    while counter:
        if counter == 1:
            thread.exit()
        time.sleep(delay)
        print "%s %s" % (threadName, time.ctime(time.time()))
        counter -= 1

threadLock = threading.Lock()

#创建新线程
thread1 = myThread(1, 'Thread-1', 1)
thread2 = myThread(2, 'Thread_2', 2)

#启动线程
thread1.start()
thread2.start()

threads = []
#添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

#等待所有线程完成
for t in threads:
    t.join()

#主线程即将退出
print "Exiting Main Thread"

'''
class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print "Starting " + self.name
        # 获得锁，成功获得锁定后返回True
        # 可选的timeout参数不填时将一直阻塞直到获得锁定
        # 否则超时后将返回False
        threadLock.acquire()
        print_time(self.name, self.counter, 3)
        # 释放锁
        threadLock.release()

def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print "%s: %s" % (threadName, time.ctime(time.time()))
        counter -= 1

threadLock = threading.Lock()
threads = []
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成
for t in threads:
    t.join()
print "Exiting Main Thread"
'''

