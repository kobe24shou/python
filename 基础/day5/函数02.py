#!/usr/bin/env python
# -*- codeing: utf-8 -*-
# Author:ls 
# aishou24@gmail.com
# date:2018/5/22

def f(*args):
    print(args)

f(*[1,2,3])  #(1, 2, 3)
f([1,2,3])  #([1, 2, 3],)


def w(**rgs):
    print(rgs)

w(**{'name':'alex'}) # 拿到是字典

print("-----------------高阶函数---------------------------------")
#高阶函数
#高阶函数是至少满足下列一个条件的函数:
#接受一个或多个函数作为输入
#输出一个函数

def add(x, y, f):
    return f(x) + f(y)
res = add(3, -6, abs)
print(res)

def foo():
    x=3
    def bar():
        return x
    return bar
