#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:ls 
# aishou24@gmail.com
# date:2018/6/5

# 函数即对象
def foo():
    print('i am the foo')
    bar()


def bar():
    print('i am the bar')
foo()


def foo():
    print('foo')
barxx = foo #  对象能赋值
barxx()
foo()
print(id(foo), id(barxx))

