#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:ls 
# aishou24@gmail.com
# date:2018/6/29
# python 生成example.ini 配置文件
# 对配置文件的增删改查

import configparser
# 文件句柄
config = configparser.ConfigParser()

config["DEFAULT"] = {'ServerAliveInterval': '45',
                     'Compression': 'yes',
                     'CompressionLevel': '9'}

config['bitbucket.org'] = {}  # 空字典
config['bitbucket.org']['User'] = 'hg' # 字典里面加键值对
config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Host Port'] = '50022'  # mutates the parser
topsecret['ForwardX11'] = 'no'  # same here
config['DEFAULT']['ForwardX11'] = 'yes'
with open('example.ini', 'w') as configfile:
    config.write(configfile)  #  config.write 写到配置文件里面

#读取 配置文件
print(config.read('example.ini'))
print(config.sections())
print(config['bitbucket.org']['User'])
print("-----------------------------------------------")
for key in config['bitbucket.org']:
    print(key)