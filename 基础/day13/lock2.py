#!/usr/bin/env python
# -*-coding:utf-8-*-
# date:2018/7/31
# 同步锁

import time
import threading

def addNum():
    global num #在每个线程中都获取这个全局变量
    # num-=1
    lock.acquire() # 获取锁
    temp=num
    print('--get num:',num )
    time.sleep(1)
    num =temp-1 #对此公共变量进行-1操作
    lock.release() # 释放锁

num = 100  #设定一个共享变量
thread_list = []
lock=threading.Lock()

for i in range(100):
    t = threading.Thread(target=addNum)
    t.start()
    thread_list.append(t)

for t in thread_list: #等待所有线程执行完毕
    t.join()

print('final num:', num )