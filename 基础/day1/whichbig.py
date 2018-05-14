#!/usr/bin/env python
# -*- codeing: utf-8 -*-
# Author:ls 
# aishou24@gmail.com
# 输入3个数字，返回最大数字

num1 = input("Num1:")
num2 = input("Num2:")
num3 = input("Num3:")

max_num = 0

if num1>num2:
    max_num= num1
    if max_num > num3:
        print("Max NUM is",max_num)
    else:
        print("Max NUM is",num3)
else:
    max_num = num2
    if max_num > num3:
        print("Max NUM is",max_num)
    else:
        print("Max NUM is",num3)
'''
num += 1  等价于 num = num + 1
num -= 1  等价于 num = num - 1
num *= 2  等价于 num = num * 2
num /= 2  等价于 num = num / 2
num //= 2  等价于 num = num // 2
num %= 2  等价于 num = num % 2
num **= 2  等价于 num = num ** 2
'''

print("h" in "hello"  ) #“h” 在“Hello” 中，判断后结果为True
print("h" not in "hello" ) # 这里的意思是 “h” 不在“Hello” 中，判断后结果为False

#身份运算符： is、is not（讲数据类型时讲解，一般用来判断变量的数据类型）