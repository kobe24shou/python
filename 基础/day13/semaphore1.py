#!/usr/bin/env python
# -*-coding:utf-8-*-
# date:2018/8/1
# 信号量
import threading,time

class myThread(threading.Thread):
    def run(self):
        if semaphore.acquire():
            print(self.name)
            time.sleep(5)
            semaphore.release()

# 信号量用来控制线程并发数的，BoundedSemaphore或Semaphore管理一个内置的计数器，
# 每当调用acquire()时-1，调用release()时+1
# BoundedSemaphore与Semaphore的唯一区别在于前者将在调用release()时检查计数器的值是否超过了计数器的初始值，如果超过了将抛出一个异常
if __name__=="__main__":
    semaphore=threading.Semaphore(5)
    thrs=[]
    for i in range(23):
        thrs.append(myThread())
    for t in thrs:
        t.start()