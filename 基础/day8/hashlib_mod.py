#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:ls 
# aishou24@gmail.com
# date:2018/6/10
#加密
import hashlib
import sha

m = hashlib.md5() #
print(m) #<md5 HASH object @ 0x00000231930DE440>

m.update("helloword".encode('utf8'))  # 把 helloword 使用md5 加密
print(m.hexdigest())  #16 进制

m.update("llxx".encode('utf8'))  #
print(m.hexdigest())  #

m2 = hashlib.md5()
m2.update("hellowordllxx".encode('utf8'))  #
print(m2.hexdigest())

