#!/usr/bin/env python
# -*- codeing: utf-8 -*-
# Author:ls 
# aishou24@gmail.com
# date:2018/5/4

def show_shopping_car():
    saving = 1000000
    shopping_car = [
        ('Mac', 9000),
        ('kindle', 800),
        ('tesla', 100000),
        ('Python book', 105),
    ]
    print('您已经购买的商品如下'.center(50, '*'))
    for i, v in enumerate(shopping_car, 1):
        print('\033[35;1m %s:  %s \033[0m' % (i, v))

    expense = 0
    for i in shopping_car:
        expense += i[1]
    print('\n\033[32;1m您的余额为 %s \033[0m' % (saving - expense))


show_shopping_car()