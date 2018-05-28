#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:ls 
# aishou24@gmail.com
# date:2018/1/10

_user ="ls"
_passwd="123"
# for 循环
for i in range(3):
    username = input("Username:")
    password = input("Password:")
    if username == _user and password ==_passwd:
        print("ok")
        break # 输入3次后 跳出 中断
    else:
        print("no")

