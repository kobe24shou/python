#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:ls 
# aishou24@gmail.com
# date:2018/6/10
import logging


#  配置日志级别，日志格式，输出位置
logging.basicConfig(level=logging.DEBUG,  # 日志级别debug
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='test.log',
                    filemode='a')  #  w 或 a 模式
# Sun, 10 Jun 2018 16:56:33 logging_mod.py[line:15] DEBUG debug message
logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')

