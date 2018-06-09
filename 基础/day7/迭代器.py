#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:ls 
# aishou24@gmail.com
# date:2018/6/9

#生成器都是迭代器，迭代器不一定是生成器

l = [1,2,4,5]
d = iter(l)   # iter 返回迭代器对象
print(d) # <list_iterator object at 0x000001A6DD27F1D0>

#迭代器满足的2个条件--》1.有iter方法，2.有next方法

print(next(d))
print(next(d))



