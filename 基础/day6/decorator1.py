#!/usr/bin/env python
# -*-coding:utf-8-*-
import  time

def foo(): #ԭ���ĺ���
    print('foo......')
    time.sleep(2)

def show_time(f):  # show_time ������װ��������

    def inner():
        start = time.time()
        f()
        end = time.time()
        print("spend %s" % (end - start))

    return  inner

foo=show_time(foo)
foo() #ִ��inner ����


