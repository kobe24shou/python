#!/usr/bin/env python
# -*-coding:utf-8-*-
# date:2018/7/30
import time
import threading

begin = time.time()
def foo(n):
    print("foo%s"%n)
    time.sleep(1)
    print("end foo")

def bar(n):
    print("bar%s"%n)
    time.sleep(2)
    print("end bar")
# foo(3)
# bar(3)

t1 = threading.Thread(target=foo,args=(1,)) # 创建线程对象
t2 = threading.Thread(target=bar,args=(2,))

t1.start()
t2.start()

print("....in the main....")

t1.join()
t2.join()

end = time.time()
print(begin-end)

