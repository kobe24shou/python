#!/usr/bin/env python
# -*-coding:utf-8-*-

import socket

sk = socket.socket()
print(sk)
address = ('127.0.0.1', 8000)
sk.connect(address)

data = sk.recv(1024)  # 阻塞住
print(str(data, "utf8"))

sk.close()
