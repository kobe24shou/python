#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:ls 
# aishou24@gmail.com
# date:2018/6/9

a = [x for x in range(10)]
b = [x*2 for x in range(10)]
c = [x*x for x in range(10)]
# 执行的顺序是先到 for x in range(10) 取元素
# 然后对取出的元素逐次进行操作 x*x 

print(a)
print(b)
print(c)


