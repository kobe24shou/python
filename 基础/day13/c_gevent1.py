#!/usr/bin/env python
# -*-coding:utf-8-*-
# date:2018/8/7

import gevent
import time

def func1():
    print('\033[31;1m李闯在跟海涛搞...\033[0m', time.ctime())
    gevent.sleep(2)  # 使用 sleep 模拟IO 阻塞状态
    print('\033[31;1m李闯又回去跟继续跟海涛搞...\033[0m', time.ctime())


def func2():
    print('\033[32;1m李闯切换到了跟海龙搞...\033[0m', time.ctime())
    gevent.sleep(1)
    print('\033[32;1m李闯搞完了海涛，回来继续跟海龙搞...\033[0m', time.ctime())


gevent.joinall([
    gevent.spawn(func1),
    gevent.spawn(func2),
    # gevent.spawn(func3),
])