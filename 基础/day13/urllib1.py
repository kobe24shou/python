#!/usr/bin/env python
# -*-coding:utf-8-*-
# date:2018/8/7

from urllib.request import urlopen
import gevent

def f(url):
    print("GET: %s" %url)
    resp = urlopen(url)
    data = resp.read()
    with open("xx.html","wb") as f:
        f.write(data)

    print("%d bytes received from %s" %(len(data), url))

f('http://www.ifeng.com/?_zbs_firefox_gg')
f('http://www.ifeng.com/?_zbs_firefox_gg')
f('http://www.ifeng.com/?_zbs_firefox_gg')


# 这种方式 gevent.joinall 快很多

gevent.joinall([
    gevent.spawn(f,'http://www.ifeng.com/?_zbs_firefox_gg'),
    gevent.spawn(f, 'http://www.ifeng.com/?_zbs_firefox_gg'),
    gevent.spawn(f, 'http://www.ifeng.com/?_zbs_firefox_gg')
])

