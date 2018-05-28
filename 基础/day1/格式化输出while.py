#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:ls 
# aishou24@gmail.com

height = int(input("Height:"))  # 用户输入一个高度
width = int(input("width:"))   # 用户输入一个宽度
# while 嵌套循环
num_height = 1
while num_height <=height:
    num_width = 1
    while num_width <= width:
        print("#", end="")
        num_width += 1
    print()
    num_height += 1

