#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:ls 
# aishou24@gmail.com
# date:2018/5/10

x = int(2.9)  # int built-in
g_count = 0  # global
def outer():
    o_count = 1  # enclosing
    def inner(): #嵌套函数
        i_count = 2  # local
        print(o_count)
    # print(i_count) 找不到
    inner()
outer()
# print(o_count) #找不到

# t = 10
# def test():
#     print(t)
#     #t=t+1 #全局变量 局部不能修改
# test()


t1 = 10
def test1():
    global t1
    print(t1)
    t1=t1+1 #global 关键字 全局变量 局部就可以修改了
test1()