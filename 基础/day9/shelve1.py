#!/usr/bin/env python
# -*-coding:utf-8-*-

import shelve

f = shelve.open(r'shelve.txt')

f['stu1_info']={'name':'alex','age':'18'}
f['stu2_info']={'name':'alvin','age':'20'}
f['school_info']={'website':'oldboyedu.com','city':'beijing'}

# f.close()

print(f.get('stu1_info')['age'])

