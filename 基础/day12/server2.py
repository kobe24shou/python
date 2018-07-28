#!/usr/bin/env python
# -*-coding:utf-8-*-
import socket

sk = socket.socket()

print(sk)
address = ('127.0.0.1', 8000)   #
sk.bind(address)  # 绑定服务端IP 地址和端口

sk.listen(3)  # 决定 server 端能容量多少排队的人数
print("waiting...........")

conn, addr = sk.accept()

while True:
    data = conn.recv(1024)
    if not data:break
    print(str(data, "utf8"))
    inp = input(">>>服务端>>>>")
    conn.send(bytes(inp, "utf8"))

conn.close()
