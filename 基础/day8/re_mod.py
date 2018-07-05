#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:ls 
# aishou24@gmail.com
# date:2018/6/29

# 正则表达式
import re

s = 'hello world llo'
print(s.find('llo'))
print(s.strip("x"))

# sring提高的方案是完全匹配

# 前面是匹配规则 后面是字符串
ret = re.findall('w\w{2}l','hello world llo')
print(ret)

ret1 = re.findall('ale','helloalexworldalexllo')
print(ret1)

# '.'     默认匹配除\n之外的任意一个字符，若指定flag DOTALL,则匹配任意字符，包括换行
ret2 = re.findall('a..e','helloalexworldalaxxexllo')  # . 匹配一位任意字符
print(ret2)

# '^'     匹配字符开头，若指定flags MULTILINE,这种也可以匹配上(r"^a","\nabc\neee",flags=re.MULTILINE)
ret3 = re.findall('^a..e','helloalexworldalaxxexllo')
print(ret3)

#'$'     匹配字符结尾，或e.search("foo$","bfoo\nsdfsf",flags=re.MULTILINE).group()也可以
ret4 = re.findall('a..e$','helloalexworldalaxxexlloa45e')
print(ret4)

# '*'     匹配*号前的字符0次或多次，re.findall("ab*","cabb3abcbbac")  结果为['abb', 'ab', 'a']
ret5 = re.findall("ab*","cabb3abcbbac")
print(ret5)

ret6 = re.findall("0*","cabb3abcbbac")
print(ret6)

# '+'     匹配前一个字符1次或多次，re.findall("ab+","ab+cd+abb+bba") 结果['ab', 'abb']
ret5 = re.findall("ab+","cabb3abcbbac")
print(ret5)

#'?'     匹配前一个字符1次或0次
ret6 = re.findall("a?b","caabbb3abcbbac")
print(ret6)

# '{m}'   匹配前一个字符m次
ret7 = re.findall("a{5}b","caaaaaaabbb3avvvvvvvbcbbac")
print(ret7)

#[c,d]  c 或者 d
ret8 = re.findall("a[c,d]x","adx")
print(ret8)

# []字符集，取消元字符的特殊功能
ret9 = re.findall("[a-z]","adz")
print(ret9)

# ^ 尖括号 放在[] 表示取反
ret10 = re.findall("[^t,6]","iutxyu56")
print(ret10)

# '\A'    只从字符开头匹配，re.search("\Aabc","alexabc") 是匹配不到的
# '\Z'    匹配字符结尾，同$
# '\d'    匹配数字0-9
# '\D'    匹配非数字
# '\w'    匹配[A-Za-z0-9]
# '\W'    匹配非[A-Za-z0-9]

ret11 = re.findall("\d{11}","iutxyusdfds12fsdfdsfs3272835465465465465428756")
print(ret11)

ret12 = re.findall(r"\\","abc\de")
print(ret12)

ret13 = re.findall(r"\b","blow")
print(ret13)

ret14 = re.findall(r"\d","ww2e5e")
print(ret14)

ret15 = re.findall("\d","ww2e5e")
print(ret15)

ret16 = re.search("(?P<province>[0-9]{4})(?P<city>[0-9]{2})(?P<birthday>[0-9]{4})","371481199306143242").groupdict("city")
print(ret16)


ret17 = re.search("(as)|3","as3").groupdict()
print(ret17)


ret18 = re.match('edf','ww2eedf5e')
print(ret18)


obj = re.compile('\.com') # 编译
ret19 = obj.findall('fadfs.comsdfdsfadsf')
print(ret19)