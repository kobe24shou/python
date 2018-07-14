#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:ls 
# aishou24@gmail.com
# date:2018/6/5

#其可以被定义在另外一个函数内(作为参数&作为返回值),类似于整形，字符串等对象
# *******函数名作为参数**********
def foo(func):
    print('foo')
    func()
def bar():
    print('bar')
foo(bar)

# *******函数名作为返回值*********
def foo():
    print('foo')
    return bar
def bar():
    print('bar')
b = foo()
b()

# 函数都是指函数名，比如foo；而foo()已经执行函数了，foo()是什么类型取决于return的内容是什么类型

