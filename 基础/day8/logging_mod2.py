#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:ls 
# aishou24@gmail.com
# date:2018/6/10
# 日志输出到文件并且输出到屏幕

import logging

logger = logging.getLogger() # 拿到logger 对象
# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('test1.log')  # 文件输出流对象

# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler() # 屏幕输出对象

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fh.setFormatter(formatter)  # 屏幕和文件的打印格式
ch.setFormatter(formatter)

logger.addHandler(fh) #logger对象可以添加多个fh和ch对象
logger.addHandler(ch)

logger.debug('logger debug message')
logger.info('logger info message')
logger.warning('logger warning message')
logger.error('logger error message')
logger.critical('logger critical message')
