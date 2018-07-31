#!/usr/bin/env python
# -*-coding:utf-8-*-
# date:2018/7/31
# 线程不安全
import time
import threading

def addNum():
    global num #在每个线程中都获取这个全局变量
    # num-=1
    temp=num
    print('--get num:',num )
    time.sleep(0.0001)
    num =temp-1 #对此公共变量进行-1操作


num = 100  #设定一个共享变量
thread_list = []
for i in range(100):    # 创建100 个线程
    t = threading.Thread(target=addNum)
    t.start()
    thread_list.append(t) # 100个线程对象加入到list里面

for t in thread_list: #等待所有线程执行完毕
    t.join()

print('final num:', num )

# 1:  why num-=1没问题呢？这是因为动作太快(完成这个动作在切换的时间内)
# 2： if sleep(1),现象会更明显，100个线程每一个一定都没有执行完就进行了切换，我们说过sleep就等效于IO阻塞，
# 1s之内不会再切换回来，所以最后的结果一定是99.