#!/usr/bin/env python
# -*- codeing: utf-8 -*-
# Author:ls 
# aishou24@gmail.com
# date:2018/1/10

_user ="ls"
_passwd = "123"
counter = 0
while counter <3:
    username = input("Username:")
    password = input("Password:")
    if username == _user and password == _passwd :
        print("Welcome %s login...." % _user)
        break #跳出，中断
    else:
        print("Invalid username or password !")
    counter += 1
    if counter == 3:
        keep_going_choice = input("还想玩么?[y/n]")
        if keep_going_choice == "y":
            counter = 0

else:
    print("要不要脸，臭流氓啊，小虎。")