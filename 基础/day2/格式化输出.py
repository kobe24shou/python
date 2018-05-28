#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:ls 
# aishou24@gmail.com
# date:2018/1/10

name = input("Nmae:")
age = int(input("Age:"))
job = input("Job:")
salary = input("Salary:")

if salary.isdigit(): #长的像不像数字,比如200d , '200'
    salary = int(salary)
else:
    #print()
    exit("must input digit") #退出程序

#格式化输出占位符的使用
msg = '''
--------- info of %s --------
Name: %s
Age : %d
Job : %s
Salary: %f
You will be retired in %s years
----------- end --------------
''' % (name,name ,age ,job ,salary, 65-age )

print(msg)