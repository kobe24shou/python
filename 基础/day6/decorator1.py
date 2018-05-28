#!/usr/bin/env python
# -*-coding:utf-8-*-
import time

def foo():# 原来的函数
    print('foo......')
    time.sleep(2)

def show_time(f):  # show_time 函数是装饰器函数

    def inner():
        start = time.time()
        f()
        end = time.time()
        print("spend %s" % (end - start))

    return inner

foo = show_time(foo)
foo() # 执行inner 函数


