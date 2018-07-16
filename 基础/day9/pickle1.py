#!/usr/bin/env python
# -*-coding:utf-8-*-
# ----------------------------pickle 序列化
import pickle

dic = {'name': 'alvin', 'age': 23, 'sex': 'male'}

print(type(dic))  # <class 'dict'>

j = pickle.dumps(dic)
print(type(j))  # <class 'bytes'>

f = open('序列化对象_pickle', 'wb')  # 注意是w是写入str,wb是写入bytes,j是'bytes'
f.write(j)  # -------------------等价于pickle.dump(dic,f)

f.close()
# -------------------------反序列化

f = open('序列化对象_pickle', 'rb')

data = pickle.loads(f.read())  # 等价于data=pickle.load(f)

print(data['age'])

# pickle 序列化 函数


def foo():
    print("ok!")


d = pickle.dumps(foo)  # pickle 写的东西看不了
f = open('序列化对象_pickle_foo', 'wb')  # 注意是w是写入str,wb是写入bytes,j是'bytes'
f.write(d)
f.close()

f = open('序列化对象_pickle_foo', 'rb')
dd = f.read()
dd = pickle.loads(dd)
dd()  # ok! 直接执行了 foo() 这个函数
