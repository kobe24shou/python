#!/usr/bin/env python
# -*-coding:utf-8-*-


class Bar:

    def foo(self, arg):
        print(self, arg)


z1 = Bar()
print(z1)   # <__main__.Bar object at 0x0000000002860C50>
z1.foo(444)  # <__main__.Bar object at 0x0000000002860C50> 444

z2 = Bar()
print(z2)   # <__main__.Bar object at 0x0000000001FC0DA0>
z2.foo(999)  # <__main__.Bar object at 0x0000000001F90DA0> 999


