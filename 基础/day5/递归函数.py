#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:ls 
# aishou24@gmail.com
# date:2018/5/24
#定义：在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。

#阶层效果
def factorial(n):
    result = n
    for i in range(1, n):
        result *= i
    return result
print(factorial(3))


# **********递归*********
def factorial_new(n):
    if n == 1: # 这个是递归条件的结束条件
        return 1
    return n * factorial_new(n - 1)
print(factorial_new(3))