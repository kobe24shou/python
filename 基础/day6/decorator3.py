#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:ls 
# aishou24@gmail.com
# date:2018/5/28

# 带参数的装饰器
import time

def show_time(func):
    def wrapper(a, b):
        start_time = time.time()
        func(a, b)
        end_time = time.time()
        print('spend %s' % (end_time - start_time))

    return wrapper


@show_time  # add=show_time(add)
def add(a, b):
    time.sleep(1)
    print(a + b)

add(2, 4)