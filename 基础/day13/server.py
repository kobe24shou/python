#!/usr/bin/env python
# -*-coding:utf-8-*-
# date:2018/7/30
# 简单并发实例

import socketserver

class MyServer(socketserver.BaseRequestHandler): # 继承类

    def handle(self): # 重写父类的方法 类名 必须是 handle
        print ("服务端启动...")
        while True:
            conn = self.request  # 拿到conn
            print (self.client_address)
            while True:
                client_data=conn.recv(1024)  # 服务端 一收一发   客户端 一发一收
                print (str(client_data,"utf8"))
                print ("waiting...")
                conn.sendall(client_data)
            conn.close()

if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1',8091),MyServer)
    server.serve_forever() # 会执行 handle 方法