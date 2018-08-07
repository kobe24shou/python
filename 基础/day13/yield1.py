#!/usr/bin/env python
# -*-coding:utf-8-*-
# date:2018/8/7
# yield 协程并发效果
import time
import queue


def consumer(name):
    print("--->starting eating baozi...")
    while True:
        new_baozi = yield  # 生成器
        print("[%s] is eating baozi %s" % (name, new_baozi))
        #time.sleep(1)


def producer():
    r = con.__next__() # r 是 yield的返回值  这里等价如  next(con)  输出 --->starting eating baozi...
    r = con2.__next__()
    n = 0
    while n < 5:
        n += 1
        con.send(n)  # new_baozi =1  然后  遇到yield 推出
        con2.send(n) # new_baozi =2
        print("\033[32;1m[producer]\033[0m is making baozi %s" % n)


if __name__ == '__main__':
    con = consumer("c1") # 这里仅仅创建一个生成器对象
    con2 = consumer("c2")  # 这里仅仅创建一个生成器对象
    p = producer()   # 执行 producer 函数  p 是函数的返回值
