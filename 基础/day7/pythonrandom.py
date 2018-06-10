#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:ls 
# aishou24@gmail.com
# date:2018/6/10

import  random

print(random.random())  #  0 到1 的随机数
print(random.randint(1,8))  #  1到8 的整数

print(random.choice('hello'))  #  获取随机字母

print(random.choice(['123',4,[15,6]]))  #  获取随机字母

print(random.sample(['123',4,99,[15,6]],2))

print(random.randrange(1,4))
print(chr(66))

def v_code():
    code = ''
    for i in range(5):
        if  i  == random.randint(0,3): #随机生成数字位数
            add = random.randrange(10)
        else:
            add = chr(random.randrange(65,91))
        code += str(add)
    print(code)


def v_code1():
    code1 = ''
    for i in range(5):
        add1 = random.choice([random.randrange(10), chr(random.randrange(65, 91))])
        code1 += str(add1)
    print(code1)

v_code()
v_code1()