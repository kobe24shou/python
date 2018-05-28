#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:ls 
# aishou24@gmail.com
# date:2018/3/14

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

#三级菜单，可以一层一层的进入所有层
#可以在每层返回上一层
#可以在任意层退出 主菜单

back_flag=False  #标记位用于返回或退出循环



while True:
    for key in menu:
        print(key)
    choice = input("1>>:".strip()) #strip() 去重或换行
    if choice in menu:
        while True:# 让程序停在第2层
            for key2 in  menu[choice]:
                print(key2)
            choice2 = input("2>>:".strip())
            if choice2 in menu[choice]:
                while True:  # 让程序停在第3层
                    for key3 in  menu[choice][choice2]:
                        print(key3)
                    choice3 = input("3>>:".strip())
                    if choice3 in menu[choice][choice2]:
                        while True:  # 让程序停在第4层
                            for key4 in menu[choice][choice2][choice3]:
                                print(key4)
                            choice4 = input("4>>:".strip())
                            print("last level")
