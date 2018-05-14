#!/usr/bin/env python
# -*- codeing: utf-8 -*-
# Author:ls 
# aishou24@gmail.com
line = 5
while line > 0:
    tmp = line
    while tmp > 0:
        print("#",end="") # 加end=""输出后面不换行
        tmp = tmp -1
    #print(line)
    print() # 输出换行
    line -= 1

#9*9 乘法表
first = 1
while first <= 9:
    sec = 1
    while sec <= first:
        print(str(sec) + "*" + str(first) + "=" + str(sec * first), end="\t") # /t 制表符 对齐
        sec += 1
    print()
    first += 1