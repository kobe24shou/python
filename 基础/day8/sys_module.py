#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:ls 
# aishou24@gmail.com
# date:2018/6/28

# sys 模块是跟python 解析器进行交互

# sys.argv           # 命令行参数List，第一个元素是程序本身路径
# sys.exit(n)        # 退出程序，正常退出时exit(0)
# sys.version        # 获取Python解释程序的版本信息
# sys.maxint         # 最大的Int值
# sys.path           # 返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
# sys.platform       # 返回操作系统平台名称
# sys.stdout.write('please:')
# val = sys.stdin.readline()[:-1]

import sys
print(sys.argv) #第一个参数是文件名  第二个元素是第二个元素

def post():
    print("post")

def download():
    print("download")

if sys.argv[1] == 'post':
    post()
elif sys.argv[1] == 'downlaod':
    download()

# E:\git\python\基础\day8>python sys_module.py post
# ['sys_module.py', 'post']
# post

