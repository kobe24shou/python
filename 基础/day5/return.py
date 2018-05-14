#!/usr/bin/env python
# -*- codeing: utf-8 -*-
# Author:ls 
# aishou24@gmail.com
# date:2018/5/10

def f():
    print('ok')
    return  10
#return 作用1.结束函数 2.返回某个对象
a=f()
print(a)

# 1.函数在执行过程中只要遇到return语句，就会停止执行并返回结果，so 也可以理解为 return 语句代表着函数的结束
# 2.如果未在函数中指定return,那这个函数的返回值为None
# 3.return多个对象，解释器会把这多个对象组装成一个元组作为一个一个整体结果输出。

def add(*args):
    print(args)
    sum=0
    for i in args:
        sum+=i
    print(sum)
    return  sum
a=add(1,2,3)
print(a)