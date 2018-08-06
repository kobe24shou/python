#!/usr/bin/env python
# -*-coding:utf-8-*-
# date:2018/8/3

f = open('text','rb')
print(f.read()) # b'\xe4\xb8\xad\xe5\x8d\x8e\xe4\xba\xba\xe6\xb0\x91\xe5\x85\xb1\xe5\x92\x8c\xe5\x9b\xbd'

f1 = open('text','r',encoding='utf8')
print(f1.read()) # 中华人民共和国

s ='中国'
print(len(s))
print(type(s))
print(repr(s))

s1 =u'中国'
print(len(s1))
print(type(s1))
print(repr(s1))
