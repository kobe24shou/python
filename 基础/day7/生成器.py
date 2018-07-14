#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:ls 
# aishou24@gmail.com
# date:2018/6/9

# generator 是生成器
# 取到的是对象，生成器的值还没有生成
# () 和 [] 区别相当于一个是全部分配到内存，一个是按next取值

a = [x*2 for x in range(10)] # 1000000--》100万数字放内存直接把电脑卡死

# 生成器的两种创建方式
# 1.小括号()
# 2.yield
s = (x*2 for x in range(10)) # 这个只是生成一个生成器的对象
print(s) # <generator object <genexpr> at 0x00000279D52F2EB8>
print(a)

print(next(s)) # 等i价于 print(s.__next__())

# 生成器是可迭代对象
for i in s: # for 循环其实是一直调用 next 值
    print(i)

def foo1():
    print("foo1")
    return 1
print(foo1())

# 只要有yield 就是一个生成器函数
def foo():   # foo() 就是一个生成器对象
    print("foo")   # 这个print没有执行
    yield 1
    print("foo yield")   # 这个print没有执行
    yield 2

g = foo()

print(foo())  # <generator object foo at 0x00000253EAA201A8>
print(next(foo()))   # foo yield 不会打印
print("---------------------------------")
next(g)   # foo yield 不会打印
next(g)   # foo yield 打印
print("---------------------------------")
# 0 1 1 2 3 5 8
def fib(max):
    n,before,after = 0,0,1
    while n < max:
        print(after)
        before,after=after,before+after
        n = n +1
fib(10)

print("---------------------------------")

def fib1(max):  # fib1 变成了生成器对象
    n,before,after = 0,0,1
    while n < max:
        yield before
        before,after=after,before+after
        n = n +1
print(fib1(10))
g = fib1(10)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
