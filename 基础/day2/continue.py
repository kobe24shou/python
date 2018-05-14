#!/usr/bin/env python
# -*- codeing: utf-8 -*-
# Author:ls 
# aishou24@gmail.com
# date:2018/1/18
for i in range(10):
    if i < 5:
        continue  # continue 结束本次循环，继续下一次循环 break 跳出整个当前循环
    print(i)  #直接从 5 开始打印

print("---------------------------------------------")
for i1 in range(10):
    if i1 < 5:
        continue
    print(i1)
    for j in range(10):
        print("layer2",j)
        if j == 6:
            break  #跳出本次循环，不是跳出外面的循环