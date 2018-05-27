#!/usr/bin/env python
# -*-coding:utf-8-*-
#����һ��д��
import time

def show_time(f):  #show_time ������װ��������

    def inner():
        start = time.time()
        f()
        end = time.time()
        print("spend %s" % (end - start))

    return  inner

@show_time # �ȼ��� foo = show_time(foo)
def foo(): #ԭ���ĺ���
    print('foo......')
    time.sleep(2)

foo()