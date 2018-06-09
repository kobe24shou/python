#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:ls 
# aishou24@gmail.com
# date:2018/6/9

# generator 是生成器
# 取到的是对象，生成器的值还没有生成

a = [x*2 for x in range(10)] # 1000000--》100万数字放内存直接把电脑卡死

s = (x*2 for x in range(10)) # 这个只是生成一个生成器的对象
print(s) # <generator object <genexpr> at 0x00000279D52F2EB8>
print(a)

print(next(s)) # 等价于 print(s.__next__())



