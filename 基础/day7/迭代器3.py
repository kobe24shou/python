#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:ls 
# aishou24@gmail.com
# date:2018/6/9

user_status = False  # 用户登录了就把这个改成True


def login(func):  # 把要执行的模块从这里传进来
    _username = "a"  # 假装这是DB里存的用户信息
    _password = "123"  # 假装这是DB里存的用户信息
    global user_status

    if user_status == False:
        username = input("user:")
        password = input("pasword:")

        if username == _username and password == _password:
            print("welcome login....")
            user_status = True
        else:
            print("wrong username or password!")

    if user_status == True:
        func()  # 看这里看这里，只要验证通过了，就调用相应功能


def home():
    print("---首页----")

def america():
    # login() #执行前加上验证
    print("----欧美专区----")

def japan():
    print("----日韩专区----")

def henan():
    # login() #执行前加上验证
    print("----河南专区----")

home()
login(america)  # 需要验证就调用 login，把需要验证的功能 当做一个参数传给login
# home()
# america()
login(henan)