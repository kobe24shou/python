#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:ls 

from wsgiref.simple_server import make_server


def application(environ, start_response):
    # print(environ['PATH_INFO'])
    # path = environ['PATH_INFO']
    # start_response('200 OK', [('Content-Type', 'text/html')])
    # f1 = open("index1.html", "rb")
    # data1 = f1.read()
    # f2 = open("index2.html", "rb")
    # data2 = f2.read()
    #
    # if path == "/yuan":
    #     return [data1]
    # elif path == "/alex":
    #     return [data2]
    # else:
    #     return ["<h1>404</h1>".encode('utf8')]

    start_response('200 OK', [('Content-Type', 'text/html')])

    return [b'<h1>Hello, web!</h1>']


httpd = make_server('', 8000, application)

print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:


httpd.serve_forever()