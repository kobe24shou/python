#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:ls 
# aishou24@gmail.com

num = 1
while num <= 10:
    num += 1
    if num == 3:
        continue
    print(num)
# 输出没有1和 3 直接2 到 11
# continue 前面的代码会执行，并且结束当前循环，跳过这次循环
# continue 跳过当次循环

print("hello world.",end="_")
print("hello world.",end="#")
print("hello world.",end="__")
print("hello world.")

# 输出一行 end 后面指定用标识符区分
# \n 不可见，默认一行最后的字符      \r\n  \r


num1 = 0
# 嵌套循环用法
while num1 <= 5:
    print(num1, end="_")

    num2 = 0
    while num2 <= 7:
        print(num2, end="-")
        num2 += 1

    num1 += 1
    print()  # print(end="\n") 什么都不输出，默认换行
