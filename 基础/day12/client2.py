#!/usr/bin/env python
# -*-coding:utf-8-*-
# 一收一发持续连接
import socket

sk = socket.socket()
print(sk)
address = ('127.0.0.1', 8000)
sk.connect(address)

while True:

    inp = input(">>>客户端>>>")
    if inp == "exit":
        break
    sk.send(bytes(inp, "utf8"))  # 不能发空
    data = sk.recv(1024)  # 阻塞住
    print(str(data, "utf8"))

sk.close()
