#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:ls 
# aishou24@gmail.com
# date:2018/6/29

# 正则表达式
import re

s = 'hello world llo'
print(s.find('llo'))
print(s.strip("x"))

# sring提高的方案是完全匹配


ret = re.findall('w\w{2}l','hello world llo')
print(ret)

