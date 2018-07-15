#!/usr/bin/env python
# -*-coding:utf-8-*-


class BaseReuqest:

    def __init__(self):
        print('BaseReuqest.init')


class RequestHandler(BaseReuqest):
    def __init__(self):
        print('RequestHandler.init')  # RequestHandler.init obj = Son() 就会执行到这个
        BaseReuqest.__init__(self)  # BaseReuqest.init 调用父类的init 方法

    def serve_forever(self):
        # self,是obj
        print('RequestHandler.serve_forever')  # 3 RequestHandler.serve_forever
        self.process_request()     # 去Minx找--》process_request 而不是它下面的这个 process_request

    def process_request(self):
        print('RequestHandler.process_request')


class Minx:

    def process_request(self):
        print('minx.process_request')


class Son(Minx, RequestHandler):
    pass


obj = Son()  # 默认会执行所有的 init方法
obj.serve_forever()

# 注意看self 是谁的对象

