#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:ls 
# aishou24@gmail.com
age = 50
flag = True

while flag:
    user_input_age = int(input("Age is :"))
    if user_input_age == age:
        print("Yes")
        flag = False
    elif user_input_age > age:
        print("Is bigger")
    else:
        print("Is smaller")

print("End")

print("------------------breake 版本------------------------")
#break  # 终止
age1 = 50
# flag = True
# break
while True:
    user_input_age = int(input("Age is :"))
    if user_input_age == age1:
        print("Yes")
        break
    elif user_input_age > age1:
        print("Is bigger")
    else:
        print("Is smaller")

