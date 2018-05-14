#!/usr/bin/env python
# -*- codeing: utf-8 -*-
# Author:ls 
# aishou24@gmail.com
# date:2018/3/22
# 高大上版本，避免重复代码
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

current_layer = menu  #实现动态循环
parent_layer = [] #保存所有父级，最有一个元素永远都是父级

while True:
    for key in current_layer:
        print(key)
    choice = input(">>>:").strip()
    if  len(choice) == 0: continue
    if choice in current_layer:
        parent_layer.append(current_layer) #在进入下一层之前，把当前层（也就是下一层的父级）追加到列表中，下一次loop
        #当用户选择b 的时候，就可以直接读取列表最后一个值出来
        current_layer = current_layer[choice] #改成了子层

    elif choice == 'b':
        if parent_layer:
            current_layer = parent_layer.pop()
    else:
        print("无此项")
