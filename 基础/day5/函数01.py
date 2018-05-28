#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:ls 
# aishou24@gmail.com
# date:2018/5/4

#函数的定义
def hello():
    print('hello')

hello()  # 调用一定记得加括号
hello()

def add(x,y):  #形参
    print(x+y)
add(7,3) #实参


def hello2(index):
    print('hello %s' %index)
hello2(3)
hello2(5)

import time
times=time.strftime('%Y--%m--%d')
def f(time):
    print('Now  time is : %s'%times)
f(times)