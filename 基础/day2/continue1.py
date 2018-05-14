#!/usr/bin/env python
# -*- codeing: utf-8 -*-
# Author:ls 
# aishou24@gmail.com
# date:2018/1/18
exit_flag = False  #标记位的使用

for i in range(10):
    if i <5:
        continue
    print(i )
    for j in range(10):
        print("layer2",j)
        if j == 6:
            exit_flag = True  #标记位的使用
            break
    if exit_flag:  # 内外层关联上，内层跳出，外层也跟着跳出
        break
