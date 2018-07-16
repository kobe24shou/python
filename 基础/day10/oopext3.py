#!/usr/bin/env python
# -*-coding:utf-8-*-


class Foo:
    def __init__(self):
        self.name = 'a'
        # obj.name
        self.name_list = ['alex']

    # obj.bar()
    def bar(self):
        # self是对象
        print('bar')
    # 用于执行 obj.per
    @property
    def perr(self):

        return 123

    # obj.per = 123
    @perr.setter
    def perr(self, val):
        print(val)

    @perr.deleter
    def perr(self):

        print(666)


obj = Foo()
r = obj.perr
print(r)

