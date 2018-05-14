#!/usr/bin/env python
# -*- codeing: utf-8 -*-
# Author:ls 
# aishou24@gmail.com
# date:2018/3/21
# 代码重复太多，比较low的写法

menu = {
    '北京':{
        '朝阳':{
            '国贸':{
                'CICC':{},
                'HP':{},
                'CCTV':{},
                '渣打银行':{},
            },
            '望京': {
                '陌陌':{},
                '奔驰':{},
                '360': {},
            },
            '三里屯': {
                '优衣库':{},
                'apple':{},
            },
    },
        '昌平': {
            '沙河':{
                '老男孩':{},
                '包子':{},
    },
            '天通苑':{
                '链家':{},
                '我爱我家':{},
            },
            '回龙观':{}
    },
        '海淀': {
            '五道口':{
                'googel':{},
                '网易':{},
                'sogo':{},
            },
            '中关村':{
                'youku':{},
                'aiqyi':{},
                'tengxun':{},
            }
        }
    },
    '上海':{
        '浦东':{
            '陆家嘴':{
                'CICC':{},
                'gs':{},
                'mogen':{},
            },
            '外滩':{},
        },
        '闵行':{},
    },
    '山东':{
        '济南':{
        },
        '德州':{
            'a':{},
            'b':{},
        },
        '青岛':{},
    },
}

back_flag=False  #标记位用于返回或退出循环
exit_flag=False  #标记位退出


while not back_flag and not exit_flag:
    for key in menu:
        print(key)
    choice = input("1>>:".strip()) #strip() 去重或换行
    if choice == 'q':
        exit_flag = True
    if choice in menu:
        while not back_flag and not exit_flag:# 让程序停在第2层
            for key2 in  menu[choice]:
                print(key2)
            choice2 = input("2>>:".strip())
            if choice2 == 'b':
                back_flag = True
            if choice2 == 'q':
                exit_flag = True
            if choice2 in menu[choice]:
                while not back_flag and not exit_flag:  # 让程序停在第3层
                    for key3 in  menu[choice][choice2]:
                        print(key3)
                    choice3 = input("3>>:".strip())
                    if choice3 == 'b':
                        back_flag = True
                    if choice3 == 'q':
                        exit_flag = True
                    if choice3 in menu[choice][choice2]:
                        while not back_flag and not exit_flag:  # 让程序停在第4层
                            for key4 in menu[choice][choice2][choice3]:
                                print(key4)
                            choice4 = input("4>>:".strip())
                            print("last level")
                            if choice4 =='b':
                                back_flag = True
                            if choice4 =='q':
                                exit_flag = True
                        else:
                            back_flag = False
                else:
                    back_flag = False
        else:
            back_flag = False

