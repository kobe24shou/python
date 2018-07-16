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


class Bar2:

    def foo2(self, arg):
        print(self, self.name, arg)


z3 = Bar2()
z3.name = "xxx"
z3.foo2(888888)   # <__main__.Bar2 object at 0x00000000026769E8> xxx 888888


class Bar3:

    def __init__(self):  # init 方法 叫构造方法  内部python自动调用  init方法常常用于初始化
        print("init self")


z4 = Bar3()  # init self
print(z4)  # <__main__.Bar3 object at 0x0000000002676AC8>

print("------------Bar4---------------------")


class Bar4:
    def __init__(self, n1, n2, n3):
        self.nam1 = n1
        self.nam2 = n2
        self.nam3 = n3
        self.nam4 = n3
        self.nam5 = n3
        self.nam6 = n3

    def foo(self):
        print(self.nam1)
        print(self.nam2)


z5 = Bar4(1, 2, 3)
print(z5.nam1)
print(z5.nam2)
print(z5.nam3)
print(z5.nam4)
z5.foo()

# 使用构造方法把值封装到对象里面
print("---------使用构造方法把值封装到对象里面----------")

#  构造方法的特性，类名加括号()，会自动执行构造方法


class Person:
    def __init__(self, name, age):
        self.n = name
        self.a = age

    def show(self):
        print("%s--%s"%(self.n, self.a))


lis = Person("LISI", 18)
lis.show()  # LISI--18

hu = Person("HUSI", 99)
hu.show()  # HUSI--99

