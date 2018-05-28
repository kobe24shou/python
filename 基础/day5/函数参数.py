#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:ls 
# aishou24@gmail.com
# date:2018/5/4

def print_info(name,age):
    print('Name: %s' %name)
    print('Age:%s' %age)

print_info('xx','18')

#必需的参数
def f(name, age):
    print('I am %s,I am %d' % (name, age))
f('alex', 18)
f('alvin', 16)

#关键字参数：
def f(name, age):
    print('I am %s,I am %d' % (name, age))
# f(16,'alvin') #报错
f(age=16, name='alvin')

print("-------------------------------------------------------")
#缺省参数（默认参数）：
def print_info(name, age, sex='male'):
    print('Name:%s' % name)
    print('age:%s' % age)
    print('Sex:%s' % sex)
    return
print_info('alex', 18)
print_info('铁锤', 40, 'female')

print("-------------------------------------------------------")
#不定长参数
def add(*tuples):
    sum = 0
    for v in tuples:
        sum += v
    return sum
print(add(1, 4, 6, 9))
print(add(1, 4, 6, 9, 5))


def add(*args):
    print(args)
add(1)
add(1,2)
add(1,2,8,99)

print("---------------------------------------------------------------------------------------")

#加了星号（*）的变量名会存放所有未命名的变量参数。而加(**)的变量名会存放命名的变量参数
def print_info(**kwargs):
    print(kwargs) # kwargs是一个字典
    for i in kwargs:
        print('%s:%s' % (i, kwargs[i]))  # 根据参数可以打印任意相关信息了
    return
print_info(name='alex', age=18, sex='female', hobby='girl', nationality='Chinese', ability='Python')
print("---------------------------------------------------------------------------------------")

###########################位置
def print_info(name, *args, **kwargs):  # def print_info(name,**kwargs,*args):报错
    print('Name:%s' % name)
    print('args:', args)
    print('kwargs:', kwargs)
    return
print_info('alex', 18, hobby='girl', nationality='Chinese', ability='Python')

# print_info(hobby='girl','alex',18,nationality='Chinese',ability='Python')  #报错
# print_info('alex',hobby='girl',18,nationality='Chinese',ability='Python')   #报错
# 关于不定长参数的位置， *arge在左边，**kwargs 参数放在右边
# 如果有默认参数，就在左边
print("---------------------------------------------------------------------------------------")

#还可以这样传参
def f(*args):
    print(args)
f(*[1, 2, 5])

def f(**kargs):
    print(kargs)
f(**{'name': 'alex'})
print("---------------------------------高阶函数------------------------------------------------------")

#补充（高阶函数）：
#         高阶函数是至少满足下列一个条件的函数:
#           接受一个或多个函数作为输入
#           输出一个函数
def add(x, y, f):
    return f(x) + f(y)
res = add(3, -6, abs)
print(res)
#############################################
def foo():
    x = 3
    def bar():
        return x
    return bar
