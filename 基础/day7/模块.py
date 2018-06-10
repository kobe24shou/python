#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:ls 
# aishou24@gmail.com
# date:2018/6/9

import time
import datetime

#print(help(time))

print(time.time()) # 时间戳

# time.struct_time(tm_year=2018, tm_mon=6, tm_mday=10, tm_hour=1, tm_min=21, tm_sec=44, tm_wday=6, tm_yday=161, tm_isdst=0)
print(time.gmtime())
# time.struct_time(tm_year=2018, tm_mon=6, tm_mday=10, tm_hour=9, tm_min=27, tm_sec=58, tm_wday=6, tm_yday=161, tm_isdst=0)
print(time.localtime())  # 本地时间

curtime_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(curtime_str)

#转化为结构化时间
print(time.strptime('2018-06-10 09:51:45','%Y-%m-%d %H:%M:%S'))

a = time.strptime('2018-06-10 09:51:45','%Y-%m-%d %H:%M:%S')
print(a.tm_year)

print(time.ctime()) # 获取当前时间，格式已经定义好了

print(time.ctime(3600)) # 时间戳转换为时间
print(time.mktime(time.localtime()))  # 时间转换为时间戳

print(datetime.datetime.now())  # 获取本地时间


