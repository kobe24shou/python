#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:ls

import  queue
d = queue.Queue() # 默认队列长度无限大

d.put("a")
d.put("b")
d.put("c")

# 队列先进先出
print(d.get(1))
print(d.get(2))
print(d.get(3))