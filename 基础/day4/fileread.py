#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:ls 
# aishou24@gmail.com
# date:2018/4/23

f=open('小重山2','r',encoding='utf8')

#a=f.readline()
#print(a)
#print(a)
print("----------------------------------------")
#无论是read()还是readline(),光标会发生位置变化
print(f.readline())
print(f.readline()) # 换行
print("----------------------------------------")
print(f.read()) # 打印没有换行
print(f.read())
print("----------------------------------------")

f=open('小重山2','r',encoding='utf8')
print(f.readlines()) #获得一个列表
f.close()
print("-----------------------------------------")

t=open('小重山2','r',encoding='utf8')
for i in t.readlines():
    print(i) #每2行之间有一个空行
f.close()

print("-----------------------------------------")
t=open('小重山2','r',encoding='utf8')
for i in t.readlines():
    print(i.strip())  # 每行之间没有空行
f.close()

number = 0

print("-----------------------------------------")

t=open('小重山2','r',encoding='utf8')
for i in t.readlines():
    number += 1
    if number == 4:
        print(i.strip(),'ikeit')  # 每行之间没有空行
    else:
        print(i.strip())
t.close()
print("-----------------------------------------")


number=0
w=open('小重山2','r',encoding='utf8')
for x in w.readlines():
    number += 1
    if number == 4:
        x = '###'.join([x.strip(), ' iiiii'])  # 取代万恶的 + 号   x=x.strip()+' xxoo'
    print(x.strip())
w.close()


print("-----------------文件只读一遍，后续操作全在列表里面------------------------")

number = 0
ff=open('小重山2','r',encoding='utf8')
data=ff.readlines()    #读取文件到列表，实际是放到内存里面了
ff.close() #注意及时关闭文件
for ii in data:
    number += 1
    if number == 6:
        ii = ''.join([ii.strip(), 'iiiii'])  # 取代万恶的+
    print(ii.strip())
ff.close()
