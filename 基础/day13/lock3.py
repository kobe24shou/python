#!/usr/bin/env python
# -*-coding:utf-8-*-
# date:2018/7/31
# 线程死锁和递归锁

import threading,time

class myThread(threading.Thread):

    def doA(self):
        lockA.acquire()
        print(self.name,"gotlockA",time.ctime())
        time.sleep(3)
        lockB.acquire()
        print(self.name,"gotlockB",time.ctime())
        lockB.release()
        lockA.release()

    def doB(self):
        lockB.acquire()
        print(self.name,"gotlockB",time.ctime())
        time.sleep(2)
        lockA.acquire()
        print(self.name,"gotlockA",time.ctime())
        lockA.release()
        lockB.release()

    def run(self):
        self.doA()
        self.doB()

if __name__=="__main__":

    lockA=threading.Lock()
    lockB=threading.Lock()
    threads=[]

    for i in range(5):
        threads.append(myThread())  # 5个对象

    for t in threads:
        t.start()

    for t in threads:
        t.join()#等待线程结束，后面再讲。