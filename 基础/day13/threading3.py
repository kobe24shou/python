#!/usr/bin/env python
# -*-coding:utf-8-*-
# date:2018/7/30

import threading
from time import ctime,sleep
import time

def music(func):
    for i in range(2):
        print ("Begin listening to %s. %s" %(func,ctime()))
        sleep(4)
        print("end listening %s"%ctime())

def move(func):
    for i in range(2):
        print ("Begin watching at the %s! %s" %(func,ctime()))
        sleep(5)
        print('end watching %s'%ctime())

threads = []
t1 = threading.Thread(target=music,args=('七里香',))
threads.append(t1)
t2 = threading.Thread(target=move,args=('阿甘正传',))
threads.append(t2)

if __name__ == '__main__':

    for t in threads:
        # t.setDaemon(True)
        t.start()
        # t.join()  # join 会阻塞住
    #t1.join()
    # t2.join() #  for 循环之后开始执行 join
    # #######三种join位置结果不一样
    print ("all over %s" %ctime()) 