#!/usr/bin/env python
# -*- codeing: utf-8 -*-
# Author:ls 
# aishou24@gmail.com
# date:2018/4/26
f=open('小重山','a',encoding='utf8')
#f.truncate() #截断数据(不能在r模式下)
#在w模式下：先清空，再写，再截断
#在a模式下：直接将指定位置后的内容截断
f.truncate(5)
f.write('hello world')
f.truncate(5)
print(f.isatty())
f.close()