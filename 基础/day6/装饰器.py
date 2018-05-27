#!/usr/bin/python
#-*-coding:utf-8 -*-
# Author:ls 
# aishou24@gmail.com
# date:2018/5/24

def outer():
    x = 10
    def inner(): #条件一 : inner是内部函数
        print(x)# 条件二 : x 是外部环境的一个变量
    return  inner() #结论：内部函数inner 就是一个闭包

f=outer()

