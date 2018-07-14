#!/usr/bin/env python
# -*-coding:utf-8-*-

import sys
import os
# 找到项目相对路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

print(os.path.abspath(__file__))
print(sys.path)
print(BASE_DIR)

