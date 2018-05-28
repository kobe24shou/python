#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:ls 
# aishou24@gmail.com
# date:2018/4/24

#flush():同步吧将数据从缓存转移到磁盘上去
##进度条实例
import sys,time
for i in range(30):
    sys.stdout.write("*")
    sys.stdout.flush()
    time.sleep(0.1)

print("-----------------------------")
for i in range(30):
    print('*',end='',flush=True)
    time.sleep(0.1)