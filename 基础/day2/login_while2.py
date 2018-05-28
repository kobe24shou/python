#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:ls 
# aishou24@gmail.com
# date:2018/1/10

_user ="ls"
_passwd="123"

# passed_authentication = False #假，不成立  标记位
# #标记位用于后面的打印
# # for 循环
# for i in range(3):
#     username = input("Username:")
#     password = input("Password:")
#     if username == _user and password ==_passwd:
#         print("ok")
#         passed_authentication = True
#         break # 输入3次后 跳出 中断
#     else:
#         print("no")
# if  not passed_authentication: #只有在True的情况下，条件成立
#     print("fuck")

# 上面代码等价于下面

# for 后面也可以跟 else
for i in range(3):
    username = input("Username:")
    password = input("Password:")
    if username == _user and password ==_passwd:
        print("ok")
        break # 输入3次后 跳出 中断
    else:
        print("no")
else:
    print("fuck")