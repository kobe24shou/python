#!/usr/bin/env python
# -*- codeing: utf-8 -*-
# Author:ls 
# aishou24@gmail.com
# date:2018/5/24
#
print("-----------------------filter(function, sequence) --------------------------")
str = ['a', 'b', 'c', 'd']
def fun1(s):
    if s != 'a':  #filter 只是过滤，不会改变值，这是跟map的区别
        return s
ret = filter(fun1, str)
print(list(ret))  # ret是一个迭代器对象
print(ret)  # ret是一个迭代器对象

print("-----------------------map(function, sequence) ------------------------------")
str = ['1', '2', 'a', 'b']
def fun2(s):
    return s + "alvin"  #可以修改元素值
ret = map(fun2, str)
print(ret)  # map object的迭代器
print(list(ret))  # ['aalvin', 'balvin', 'calvin', 'dalvin']

print("-----------------------reduce(function, sequence, starting_value)　 ------------------------------")

from functools import reduce
def add1(x, y):
    return x + y
print(reduce(add1, range(1, 101)))  ## （注：1+2+...+99+100）
print(reduce(add1, range(1, 101), 20))  ## 4970 （注：1+2+...+99+20）

print("-----------------------lambda　 ------------------------------")
# 普通函数
def add(a, b):
    return a + b
print(add(2, 3))

# 匿名函数
add1 = lambda a, b: a + b
print(add1(2, 3))

print(lambda a, b: a + b)