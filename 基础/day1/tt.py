#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:ls 
# aishou24@gmail.com

a=1
b=2
if  a<b:
    print("Yes")
    print("Yes")
    print("Yes")
    print("Yes")
else:
    print("No")
a=1
b=2
if a > b:
    print("Yes")
elif a == b:
    print("第三")
else:
    print("any")

a = 999
b = 100
c = 1000

if  b <= a <= c:
    print("True")

#算数运算
print(5//2)
print(4//2)
print(9%2)
print(2**10)

num = 4
while num > 0:
    print("#",end="")
    num -= 1
print()
# 输出一行四个 # 号
num = 4
while num > 0:
    print("#")
    num -= 1
# 输出一列四行

# 循环没有被中断
num = 0
while num<10:
    num = num + 1
    if num%2 ==0:
        continue
    print(num)
else:
    print("else-----")

### 循环被中断
num = 0
while num<10:
    num = num + 1
    if num%2 ==0:
        break
    print(num)
else:
    print("else-----")
