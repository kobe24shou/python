#!/usr/bin/env python
# -*- codeing: utf-8 -*-
# Author:ls 
# aishou24@gmail.com
'''
while True:
    print("any")
    print("any")
'''
num = 1
while num < 10:
    print(num)
    num += 1

print("------------输出1-100 的偶数--------------------")
num2 = 1
while num2 < 100:
    if num2%2 == 0:
        print(num2)
    num2 += 1

print("------------输出1-100 的基数--------------------")
num3 = 1
while num3 < 100:
    if num3%2 == 1:
        print(num3)
    num3 += 1


print("------------测试 break--------------------")
num4 = 1
while num4 < 10:
    print(num4)
    num4 += 1
    if num4 == 4:
        break