#!/usr/bin/env python
# -*- codeing: utf-8 -*-
# Author:ls 
# aishou24@gmail.com
# date:2018/1/22

product_list=[ #定义一个列表,列表和元组是有顺序的
    ('Mac',9000),
    ('kindle',800),
    ('tesla',900000),
    ('python book',105),
    ('bike',2000),

]
saving=input('please input your money:')
shopping_car=[]  # 定义一个购物车
if saving.isdigit(): #只有是数字的时候，才会走下面的代码
    saving=int(saving)
    while True:  #反复提供用户商品信息列表
        #打印商品内容 遍历列表
        for i,v in enumerate(product_list,1): #in 后面加的要是一个序列 enumerate 是加序号用的   添加编号并用2个变量接收
            print(i,'>>>>',v)  # 上面用i v 2个变量去接受，更方便格式化

         #引导用户选择商品
        choice=input('选择购买商品编号[退出：q]：')

        #验证输入是否合法
        if choice.isdigit():
            choice=int(choice) #输入的字符串修改为整形数字
            if choice>0 and choice<=len(product_list):  #判断用户选择是否越界
                #将用户选择商品通过choice取出来
                p_item=product_list[choice-1] #根据编号取商品内容 包括 商品和价格

                #如果钱够，用本金saving减去该商品价格，并将该商品加入购物车
                if p_item[1]<saving: # p_item[1] 是拿到商品价格
                    saving-=p_item[1]

                    shopping_car.append(p_item)

                else:
                    print('余额不足，还剩%s'%saving)
                print(p_item)
            else:
                print('编码不存在')
        elif choice=='q':
            print('------------您已经购买如下商品----------------')
            #循环遍历购物车里的商品，购物车存放的是已买商品
            for i in shopping_car:
                print(i)
            print('您还剩%s元钱'%saving)
            break
        else:
            print('invalid input')