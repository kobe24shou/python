#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:ls 
# aishou24@gmail.com
# date:2018/7/3
import  re
source = "1-2*-30/   -12*(   -20+200*-3/-20   0*-300-100)"

def check(s):
    flag = True
    if re.findall('[a-zA-z]',s):
        print("Invalid")
        flag = False

    return  flag

def format(s):
    s = s.replace(' ','')
    s = s.replace('++','+')

    return s

def cal_mul_div(s): # (2+5*3)   乘除
    ret = re.search('\d+\.?\d*[*/]\d+\.?\d*',s)
    x,y = re.split('[*/]',ret) # 分开拿到两个数
    float(x)*float(y)
    return  s # (2+15)

def cal_add_sub(s): # (2+5)   加减

    return  s # (7)


if check(source):
    strs = format(source)
    #print(strs)

    # 处理括号
    while re.search('\('):
        strs = re.search('\([^()]\)',strs).group()
        strs = cal_mul_div(strs) # 2+15)
        strs = cal_add_sub(strs)

    else:
        strs = cal_mul_div(strs) # 2+15)
        strs = cal_add_sub(strs)










