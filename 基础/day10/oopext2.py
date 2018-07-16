#!/usr/bin/env python
# -*-coding:utf-8-*-


class Base:
    def a(self):
        print('Base.a')


class F0(Base):
    def a1(self):
        print('F0.a')


class F1(F0):
    def a1(self):
        print('F1.a')


class F2(Base):
    def a1(self):
        print('F2.a')


class S(F1,F2):
    pass


obj = S()
obj.a()

