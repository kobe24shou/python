#!/usr/bin/env python
# -*-coding:utf-8-*-
import  time

def foo():
    start = time.time()
    print('foo......')
    time.sleep(2)
    end = time.time()
    print('speed %s' %(end-start))
foo()

def show_time():  # 
    start = time.time()
    foo()
    end = time.time()
    print('speed %s' % (end - start))

def show_time2(f):  # 
    start = time.time()
    f()
    end = time.time()
    print('speed %s' % (end - start))

show_time()
print("---------------show time 2-----------------------------")
show_time2(foo)