#!/usr/bin/env python
# -*- codeing: utf-8 -*-
# Author:ls 
# aishou24@gmail.com
# date:2018/4/24

# readlines() 读取文本放入列表，然后把列表放到内存里面

##########对于大数据文件，要用以下方式（the best way）：
f=open('小重山2','r',encoding='utf8')
number=0
print(f.tell())  #取出光标位置，但是处理中文的位置有点问题

for i in f: #这是for内部将f对象做成一个迭代器，用一行去一行。
    number +=1
    if number == 6:
        i = ''.join([i.strip(), 'iiiii'])  #取代万恶的+
        print(i.strip())
print(f.tell())
f.seek(4) #调整光标到指定的位置
print(f)