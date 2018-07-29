#!/usr/bin/env python
# -*-coding:utf-8-*-
import socket
import os

sk = socket.socket()

print(sk)
address = ('127.0.0.1', 8000)
sk.bind(address)  # 绑定服务端IP 地址和端口
sk.listen(3)  # 决定 server 端能容量多少排队的人数
print("waiting...........")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


while True:
    conn, addr = sk.accept()

    while True:
        data = conn.recv(1024)
        cmd, filename, filesize = str(data,"utf8").split("|")
        path = os.path.join(BASE_DIR, "day12_2", filename)    # 上传目录
        filesize = int(filesize)

        f = open(path, "ab")
        # 循环接受
        has_receive = 0
        while has_receive != filesize:
            data = conn.recv(1024)
            f.write(data)
            has_receive += len(data)
        f.close()

sk.close()
