#!/usr/bin/env python
# -*-coding:utf-8-*-
while True:
    try:
        # 代码块，逻辑
        inp = input('请输入序号：')
        i = int(inp)
    except Exception as e:
        # e是Exception对象，对象中封装了错误信息
        # 上述代码块如果出错，自动执行当前块的内容
        print(e)
        i = 1
    print(i)

