#!/usr/bin/env python
# -*- codeing: utf-8 -*-
# Author:ls 
# aishou24@gmail.com
# date:2018/5/24
#filter(function, sequence)
str = ['a', 'b', 'c', 'd']
def fun1(s):
    if s != 'a':
        return s
ret = filter(fun1, str)
print(list(ret))  # ret是一个迭代器对象
print(ret)  # ret是一个迭代器对象