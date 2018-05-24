#!/usr/bin/env python
# -*- codeing: utf-8 -*-
# Author:ls 
# aishou24@gmail.com
# date:2018/5/24

def f(n):
    return  n*n

def foo(a,b,func):
    ret = func(a)+func(b)
    return  ret

print(foo(1,2,f))

print("-----------------------------------------------------")

x = int(2.9)  # int built-in
g_count = 0  # global
def outer():
    o_count = 1  # enclosing
    def inner():
        i_count = 2  # local
        print(o_count)
    # print(i_count) 找不到
    inner()
outer()
# print(o_count) #找不到