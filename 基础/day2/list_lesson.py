#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:ls 
# aishou24@gmail.com
# date:2018/1/18

#需求： 存储一个班的所有学生姓名
# name0='wuchao' 弊端1
# name1='jinxin'
# name2='xiaohu'
# name3='sanpang'
# name4='ligang'
#
# names="wuchao jinxing xiaohu sanpang ligang"  弊端2 不方便取

# list 列表顺应而生

list1 = ['Google', 'Runoob', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7];
a = ['A','B','C','D','E'];
print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])


#列表操作 --》增删改查
#查  切片 []  按照索引输出,下标从0开始，类似顾头不顾尾

print("9",a[0]) # 下标0开始
print("1",a[3]) # 查
print("2",a[1:4]) #取出1到 4，3个元素
print("3",a[1:])#取到最后
print("4",a[1:-1])#取到倒数第二值
print("5",a[1:-1:1])#从左到右一个一个去取
print("6",a[1::2])#从左到右隔一个去取
print("7",a[3::-1]) #从右到左隔一个一个去取
print("8",a[2:-2:-1]) #从右到左隔一个一个去取

b = a[3::-2]  # -1 是倒数第一个，-2 是倒数第2个
print("10",b) # ['D', 'C', 'B', 'A']
print(a[-2::-1])
print(a[1:-1:-2])


# 列表增加
#添加 append insert  "+" 加号也是添加

a.append('xx')  #默认插到最后一个位置
print(a)
a.insert(1,'oo') #将数据插入到任意一个位置
print(a)


#列表修改 赋值操作
a[1]='haidilao'
print(a)
a[1:3]=['a','b']
print(a)

#删除 remove pop del
print("------------------------------------------")
print("删除前",a)
a.remove(a[0])
print("删除后",a)
b=a.pop(1) #返回索引位置，默认是删除最后一个元素
print("pop删除后",a)
#
del a[0]  #删除列表
print("del后    ",a)
a.clear()  #列表清空
del a  #删除队列

print("--------------count 计算某元素出现次数 ---------------------------")
#count:计算某元素出现次数
t = ['to', 'be', 'or', 'not', 'to', 'be'].count('to')
print(t)

print("--------------extend 把 b 列表元素全部添加到 a 里面 ---------------------------")
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
c = a + b
print(a)
print(b)
print(c)


print("--------------index  根据内容找位置 ---------------------------")
a = ['wuchao', 'jinxin', 'xiaohu','ligang', 'sanpang', 'ligang', ['wuchao', 'jinxin']]
print(a.index('ligang'))  # 返回的值以第一个为主 从 0 开始

# 通过切片找到第2个 ligang
first_lg_index = a.index("ligang")
print("first_lg_index",first_lg_index)
little_list = a[first_lg_index+1:]
second_lg_index = little_list.index("ligang")
print("second_lg_index",second_lg_index)
second_lg_index_in_big_list = first_lg_index + second_lg_index +1
print("second_lg_index_in_big_list",second_lg_index_in_big_list)
print("second lg:",a[second_lg_index_in_big_list])

print("--------------reverse  反转-----------------------------")
a = ['wuchao', 'jinxin', 'xiaohu','ligang', 'sanpang', 'ligang']
a.reverse()
print(a)

print("--------------index 方法 用于列表中找出某个值第一个匹配的索引位置-------------")
a = ['wuchao', 'jinxin', 'xiaohu','ligang', 'sanpang', 'ligang']
print(a.index('ligang'))

print("--------------reverse  sort  排序---------------------------")
x = [4, 6, 2, 1, 7, 9]
print(x)
x.sort(reverse=True)
print(x)#[1, 2, 4, 6, 7, 9]

print("--------------  reverse   ---------------------------------------")
a = ['wuchao', 'jinxin', 'Xiaohu','Ligang', 'sanpang', 'ligang']
a.sort()
print("字符串排序 ",a) # 按照ask码排序

print(a.count("Xiaohu"))
print(a.pop())
print(a)