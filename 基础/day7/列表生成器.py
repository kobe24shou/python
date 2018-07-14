#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:ls 
# aishou24@gmail.com
# date:2018/6/9

def f(n):
    return  n**3

# 执行的顺序是先到 for x in range(10) 取元素
# 然后对取出的元素逐次进行操作 x*x ,操作完的结果再依次放到列表里面去

a = [x for x in range(10)]
b = [x*2 for x in range(10)]
c = [x*x for x in range(10)]
d = [f(x) for x in range(10)]

print(a)
print(b)
print(c)
print(d)
print(type(d))

t = ('123',8)
w1,w2 = t
print(w1,w2)