#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:ls 
# aishou24@gmail.com
# date:2018/7/3

import re

ret = re.findall('a..in', 'helloalvin')
print(ret)  # ['alvin']

ret = re.findall('^a...n', 'alvinhelloawwwn')
print(ret)  # ['alvin']

ret = re.findall('a...n$', 'alvinhelloawwwn')
print(ret)  # ['awwwn']

ret = re.findall('a...n$', 'alvinhelloawwwn')
print(ret)  # ['awwwn']

ret = re.findall('abc*', 'abcccc')  # 贪婪匹配[0,+oo]
print(ret)  # ['abcccc']

ret = re.findall('abc+', 'abccc')  # [1,+oo]
print(ret)  # ['abccc']

ret = re.findall('abc?', 'abccc')  # [0,1]
print(ret)  # ['abc']

ret = re.findall('abc{1,4}', 'abccc')
print(ret)  # ['abccc'] 贪婪匹配

#前面的*,+,?等都是贪婪匹配，也就是尽可能匹配，后面加?号使其变成惰性匹配
ret=re.findall('abc*?','abcccccc')
print(ret)#['ab']
# --------------------------------------------字符集[]
ret = re.findall('a[bc]d', 'acd')
print(ret)  # ['acd']

ret = re.findall('[a-z]', 'acd')
print(ret)  # ['a', 'c', 'd']

ret = re.findall('[.*+]', 'a.cd+')
print(ret)  # ['.', '+']

# 在字符集里有功能的符号: - ^ \

ret = re.findall('[1-9]', '45dha3')
print(ret)  # ['4', '5', '3']

ret = re.findall('[^ab]', '45bdha3')
print(ret)  # ['4', '5', 'd', 'h', '3']

ret = re.findall('[\d]', '45bdha3')
print(ret)  # ['4', '5', '3']

ret=re.findall('I\b','I am LIST')
print(ret)#[]
ret=re.findall(r'I\b','I am LIST')
print(ret)#['I']

#--------
ret = re.findall('c\\\l', 'abc\le')
print(ret)  # []
ret = re.findall('c\\\l', 'abc\le')
print(ret)  # []
ret = re.findall('c\\\\l', 'abc\le')
print(ret)  # ['c\\l']
ret = re.findall(r'c\\l', 'abc\le')
print(ret)  # ['c\\l']

# -----------------------------eg2:
# 之所以选择\b是因为\b在ASCII表中是有意义的
m = re.findall('\bblow', 'blow')
print(m)
m = re.findall(r'\bblow', 'blow')
print(m)

# 元字符之分组()
m = re.findall(r'(ad)+', 'add')
print(m)

ret = re.search('(?P<id>\d{2})/(?P<name>\w{3})', '23/com')
print(ret.group())  # 23/com
print(ret.group('id'))  # 23
print(ret.group('name'))  # com

# 元字符之｜
ret=re.search('(ab)|\d','rabhdg8sd')
print(ret.group())#ab

print('---------------------------------')
# 1
re.findall('a', 'alvin yuan')  # 返回所有满足匹配条件的结果,放在列表里
# 2
re.search('a', 'alvin yuan').group()
# 函数会在字符串内查找模式匹配,只到找到第一个匹配然后返回一个包含匹配信息的对象,该对象可以
# 通过调用group()方法得到匹配的字符串,如果字符串没有匹配，则返回None。

# 3
re.match('a', 'abc').group()  # 同search,不过尽在字符串开始处进行匹配

# 4
ret = re.split('[ab]', 'abcd')  # 先按'a'分割得到''和'bcd',在对''和'bcd'分别按'b'分割
print(ret)  # ['', '', 'cd']

# 5
ret = re.sub('\d', 'abc', 'alvin5yuan6', 1)
print(ret)  # alvinabcyuan6
ret = re.subn('\d', 'abc', 'alvin5yuan6')
print(ret)  # ('alvinabcyuanabc', 2)

# 6
obj = re.compile('\d{3}')
ret = obj.search('abc123eeee')
print(ret.group())  # 123

ret = re.finditer('\d', 'ds3sy4784a')
print(ret)  # <callable_iterator object at 0x10195f940>

print(next(ret).group())
print(next(ret).group())
print(next(ret).group())

ret1 = re.search('\([^()]+\)','(1+(2+5*3)*2)')
print(ret1.group()) #  (2+5)

ret2 = re.search('\d+\.?\d*[*/]\d+\.?\d*','(1+(2+5*3)*2)')
print(ret2)
