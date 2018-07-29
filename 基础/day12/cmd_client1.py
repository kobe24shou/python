#!/usr/bin/env python
# -*-coding:utf-8-*-

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

    # 循环接受，不然服务端发生太多，接受不了
    # 一次只能接受1024字节

    result_len = int(str(sk.recv(1024), "utf8"))
    print("接受长度：" + str(result_len))
    #sk.send(bytes("ok"), "utf-8")

    data = bytes()
    while len(data) != result_len:
        t_recv = sk.recv(1024)
        data += t_recv

    print(str(data, "gbk"))

sk.close()
