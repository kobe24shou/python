#!/usr/bin/env python
# -*- codeing: utf-8 -*-
# Author:ls 
# aishou24@gmail.com
# date:2018/4/26

# 终极问题 如何在磁盘修改文件
# 常规思路，由于磁盘存储机制不能完成
#
number=0
f = open('小重山2','r+',encoding='utf8')

for line in f:
    number+=1
    if number==3:
        f.write('alex')  #写是最后开始写，如果要修改其中的一行，可以曲线救国，拷贝出来，修改指定行，然后覆盖掉原文件
f.close()


#只能采取重新创建一个文件的思路
f_read=open('小重山','r',encoding='utf8')
f_write = open('小重山3','w',encoding='utf8')

number=0
for line in f_read:
    number+=1
    if number==5:#取出第5行 进行替换
        line=''.join([line.strip(),'alex\n'])
        #line='hello 岳飞\n'
    f_write.write(line)

f_read.close()
f_write.close()

#wih子句代码块会自close文件 with 同时管理多个文件对象
#with open('log','r') as f_read,open('log2','w') as f_write:
#    for line in f_read:
#       f_write.write(line)
