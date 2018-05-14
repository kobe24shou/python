#!/usr/bin/env python
# -*- codeing: utf-8 -*-
# Author:ls 
# aishou24@gmail.com
# date:2018/3/26

############################基本流程
#能调用方法的一定是对象
# import time
#三种基本的操作模式 r(只可读) w（只可写） a（追加）
#流程：1 创建文件对象 2 调用文件方法进行操作  3 关闭文件


f=open('小重山','r',encoding='utf8') # r表示对文件进行读模式的操作
# f.write()#报错
data=f.read()
print(data+"1111111111")
f.close() # 打开 操作 关闭

f=open('小重山','r',encoding='utf8') #7是取7个字符
data1 = f.read(7)
print(data1 +"22222222222")
f.close()

f=open('小重山','w',encoding='utf8') #写模式是第一步先清空内容
f.write('xxxx xxx')
f.write('\nhello world \n')
f.write('alex')
#
#注意：if not close,数据会缓存，而不是磁盘！
# time.sleep(30)






######作业涉及方法
# a=str({'beijing':{'1':111}})
# print(type(a))
# print(a)#     '{'beijing':{'1':111}}'
# a=eval(a)
# print(type(a))
# print(a['beijing'])

# f=open('log', 'r')
# f.readline()
# f.read()
# f.close()

# with open('log', 'r') as f:
#     f.readline()
#     f.read()
# print('hello')

#with 同时管理多个文件对象
# with open('log1','r') as f_read, open('log2','w') as f_write:
#     for line in f_read:
#         f_write.write(line)