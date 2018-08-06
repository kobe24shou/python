#!/usr/bin/env python
# -*-coding:utf-8-*-

from multiprocessing import Process   # 进程
import time


def f(name):
    time.sleep(1)
    print('hello', name, time.ctime())


if __name__ == '__main__':
    p_list = []
    for i in range(20):
        p = Process(target=f, args=('alvin',))   # 调用方式
        p_list.append(p)
        p.start()

    for p in p_list:
        p.join()
    print('end')

