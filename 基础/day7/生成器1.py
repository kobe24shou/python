#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:ls 
# aishou24@gmail.com
# date:2018/6/9

# send方法可以传值
def bar():
    print("okwok")
    count = yield  1  # 传进来的赋值给count了
    print(count)

    print("ok")
    yield  2

b = bar()
next(b)
s=b.send("eee")  #第一次 send 前如果没有next ，只能传一个 send(None),send(None)= next()
print(s)
