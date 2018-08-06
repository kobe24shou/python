#!/usr/bin/env python
# -*-coding:utf-8-*-
# 不同进程间的通讯

from multiprocessing import Process, Queue


def f(q, n):
    q.put([42, n, 'hello'])
    print("subprocess  q id", id(q))


if __name__ == '__main__':
    q = Queue()  # 直接创建  和线程之间的queue 没有关系
    p_list = []
    print("main q id:", id(q))

    for i in range(3):
        p = Process(target=f, args=(q, i))
        p_list.append(p)
        p.start()
    print(q.get())
    print(q.get())
    print(q.get())
    for i in p_list:
            i.join()
