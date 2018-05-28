#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:ls 
# aishou24@gmail.com
# date:2018/4/23

#####applend 在文章末尾添加文本
f=open('小重山2','a',encoding='utf8')
f.write('hello world test \n')
f.write('xx')
f.close()


# r+:光标默认在0位置，最后位置开始写
# w+:先清空，再写读
# a+:光标默认在最后位置


d=open('小重山','r+',encoding='utf8')
print(d.tell())
print(d.readline())
d.write('岳飞')
print(d.tell())
d.seek(0)
print(d.readline())
d.close()