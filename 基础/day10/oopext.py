#!/usr/bin/env python
# -*-coding:utf-8-*-


class F:

    def f1(self):
        print('F.f1')

    def f2(self):
        print('F.f2')


class S(F):
    def s1(self):
        print('S.s1')

    def f2(self):
        # obj
        print('S.f2')
        super(S, self).f2() # 执行父类（基类）中的f2方法
        F.f2(self)          # 执行父类（基类）中的f2方法


obj = S()
obj.s1()
obj.f2()

