#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:ls 
# aishou24@gmail.com
# date:2018/5/4

#列表创建的两种方式
a=[1,3,4]
b=list([4,5,6])
print(a)
print(b)

#集合的创建只有一种方式创建，通过set关键字创建
s = set('lsstta')
print(s)#集合会直接去重
print(s,type(s))

s2=list(s)
print(s2,type(s2))

#集合是无序不重复
#判断元素在不在，in or not in
s.add('u')
print(s)

s.update('ops')
print(s)

s.update('oooo')
print(s)

s.update([1,2],'ww')
print(s)

s.remove(2)
print(s)

s.pop()#随机删除
print(s)


del s









