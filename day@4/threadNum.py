#!/usr/bin/env python
# encoding: utf-8

import threading
import time

class myThread(threading.Thread):
    def run(self):
        global num

        mutex.acquire(1)
        time.sleep(1)
        num += 1
        msg = self.name + 'set num to ' + str(num)
        print msg
        mutex.release()

num = 0
mutex = threading.Lock()


def test():
    for i in range(5):
        t = myThread()
        t.start()
if __name__ == '__main__':
    test()


