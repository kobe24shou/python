#!/usr/bin/env python
# -*- codeing: utf-8 -*-
# Author:ls 
# aishou24@gmail.com
# date:2018/4/27

s = [1,'a','b']
s1 = [1,'a','b'] #比较差的方式
s2 = s.copy()
s2[0]=3

print(s)
print(s1)
print(s2)

print("------------------------------------------------------")
s4 = [[1,2],'a','b']
print(s4)
s5=s4.copy()
s5[0][1]='888' #注意这里修改了拷贝量s5 但是原来的s4 也同步修改了
print(s5)
print(s4) #原来的s4 也同步修改了
