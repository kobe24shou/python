#!/usr/bin/env python
# -*-coding:utf-8-*-

import socket
import os
sk = socket.socket()
print(sk)
address = ('127.0.0.1', 8000)
sk.connect(address)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


while True:
    inp = input(">>>客户端>>>").strip()  # 输入pos命令上传文件 post|11.png
    cmd, path = inp.split("|")

    path = os.path.join(BASE_DIR, path)

    filename = os.path.basename(path)  # 文件名
    file_size = os.stat(path).st_size  # 文件大小

    file_info = "post|%s|%s" % (filename, file_size)

    sk.sendall(bytes(file_info, "utf8"))

    # 开始发文件
    # with open(path,"rb") as f:
    f = open(path, "rb")
    has_sent = 0

    while has_sent != file_size:  # 循环发送
        data = f.read(1024)
        sk.sendall(data)
        has_sent += len(data)
    f.close()
    print("上传成功")

sk.close()
