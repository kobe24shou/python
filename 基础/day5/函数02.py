#!/usr/bin/env python
# -*- codeing: utf-8 -*-
# Author:ls 
# aishou24@gmail.com
# date:2018/5/22

def f(*args):
    print(args)

f(*[1,2,3])  #(1, 2, 3)
f([1,2,3])  #([1, 2, 3],)


def w(**rgs):
    print(rgs)

w(**{'name':'alex'}) # 拿到是字典

