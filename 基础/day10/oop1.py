#!/usr/bin/env python
# -*-coding:utf-8-*-
# 创建类


class Foo:

    def bar(self):
        print("Bar")

    def hello(self, name):
        print("i am %s" % name)


# 根据类Foo创建对象obj
obj = Foo()
obj.bar()  # 执行Bar方法
obj.hello("wupeiqi")  # 执行Hello方法　
