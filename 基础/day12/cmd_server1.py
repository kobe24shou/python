#!/usr/bin/env python
# -*-coding:utf-8-*-

import socket
import subprocess

sk = socket.socket()

print(sk)
address = ('127.0.0.1', 8000)   #
sk.bind(address)  # 绑定服务端IP 地址和端口
sk.listen(3)  # 决定 server 端能容量多少排队的人数
print("waiting...........")


while True:
    conn, addr = sk.accept()

    while True:
        try:   # 防止客户端强制退出，导致服务端挂掉
            data = conn.recv(1024)
        except Exception as e:
            break
        print(str(data, "utf8"))

        if not data:
            break
        print(".............", str(data, "utf8"))

        obj = subprocess.Popen(str(data, "utf8"), shell=True, stdout=subprocess.PIPE)
        cmd_result = obj.stdout.read()
        result_len = bytes(str(len(cmd_result)), "utf8")  # int 和bytes 不能直接转，需要str 中间过度

        conn.sendall(result_len)
        conn.sendall(cmd_result)

sk.close()
