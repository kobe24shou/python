#!/usr/bin/env python
# -*-coding:utf-8-*-
# date:2018/8/23

import socket

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost',8089))
    sock.listen(5)

    while True:
        connection, address = sock.accept()
        buf = connection.recv(1024)
        print(buf.decode('utf8')) # 打印客户端接收到的内容

        connection.sendall(bytes("HTTP/1.1 201 OK\r\n\r\n","utf8"))

        #connection.sendall(bytes("<h1>Hello,World</h1>","utf8"))
        with open('hello.html','rb') as f:   # 读取html文件内容发送
            data = f.read()
        connection.sendall(data)
        connection.close()

if __name__ == '__main__':
    main()