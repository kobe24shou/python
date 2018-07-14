#!/usr/bin/env python
# -*-coding:utf-8-*-
import json
# x="[null,true,false,1]"
# print(eval(x))

# print(json.loads(x))

# ----------------------------序列化列表，字典  dumps 进去 loads 读回来

dic = {'name': 'alvin', 'age': 23, 'sex': 'male'}   # 字典
print(type(dic))  # <class 'dict'>

j = json.dumps(dic)  # 保存json进去
print(type(j))  # <class 'str'>

f = open('序列化对象', 'w')
f.write(j)  # -------------------等价于json.dump(dic,f)
f.close()
# -----------------------------反序列化<br>  取jaon内容

f = open('序列化对象')
data = json.loads(f.read())  # 等价于data=json.load(f)
print(data)
print(data['age'])

