#!/usr/bin/env python
# -*-coding:utf-8-*-
#另外一种写法
import time

def show_time(f):  #show_time 函数是装饰器函数

    def inner():
        start = time.time()
        f()
        end = time.time()
        print("spend %s" % (end - start))

    return  inner

@show_time # 等价于 foo = show_time(foo)
def foo(): #原来的函数
    print('foo......')
    time.sleep(2)

foo()