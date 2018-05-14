#!/usr/bin/env python
# -*- codeing: utf-8 -*-
# Author:ls 
# aishou24@gmail.com
msg ='sss'
msg1="sss"
msg3="it is 'ss "
#', "" 双单引号的意义是一样的
print(msg)
print(msg1)
print(msg3)

#有限循环次数，及开始和结束的位置
for i in range(3):
    print(i)


for i in range(1,3):
    print(i)

print("-----------------------")
for i in range(1,10):
    if  i%2 == 0:
        print(i)

print("-----------------------")
for i in range(1,10,2): # 2 是指步长
        print(i)

print("-----------------------")
for i in range(100):
    if i < 50 or i > 70:
        print(i)
