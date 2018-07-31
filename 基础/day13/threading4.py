#!/usr/bin/env python
# -*-coding:utf-8-*-
# date:2018/7/31

# 继承式调用
import threading
import time


class MyThread(threading.Thread): # 先自己定义一个类
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):  # 定义每个线程要运行的函数

        print("running on number:%s" % self.num)

        time.sleep(3)


if __name__ == '__main__':
    t1 = MyThread(1)
    t2 = MyThread(2)

    t1.start() # 这里调用start的时候，就调用了 run 方法
    t2.start()