#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:ls 
# aishou24@gmail.com
# date:2018/6/5

# 函数的嵌套以及闭包
def foo():
    print('foo')
    def bar():
        print('bar')
    bar()
#bar()


# 想执行inner函数,两种方法
def outer():
    x = 1
    def inner():
        print(x)  # 1
    # inner() # 2
    return inner
# outer()
in_func = outer()
in_func()


origin = [0, 0] # 坐标系统原点
legal_x = [0, 50] # x轴方向的合法坐标
legal_y = [0, 50] # y轴方向的合法坐标
def create(pos=origin):
 def player(direction,step):
  # 这里应该首先判断参数direction,step的合法性，比如direction不能斜着走，step不能为负等
  # 然后还要对新生成的x，y坐标的合法性进行判断处理，这里主要是想介绍闭包，就不详细写了。
  new_x = pos[0] + direction[0]*step
  new_y = pos[1] + direction[1]*step
  pos[0] = new_x
  pos[1] = new_y
  #注意！此处不能写成 pos = [new_x, new_y]，原因在上文有说过
  return pos
 return player

player = create() # 创建棋子player，起点为原点
print (player([1,0],10)) # 向x轴正方向移动10步
print (player([0,1],20)) # 向y轴正方向移动20步
print (player([-1,0],10)) # 向x轴负方向移动10步

