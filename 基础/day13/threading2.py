#!/usr/bin/env python
# -*-coding:utf-8-*-
# date:2018/7/30
import  threading
import  time
begin = time.time()

def add(n):
    sum = 0
    for i in range(n):
        sum += i
    print(sum)

# add(10000000)
# add(20000000)

t1 = threading.Thread(target=add,args=(10000000,))
t1.start()

t2 = threading.Thread(target=add,args=(20000000,))
t2.start()

t1.join() # join 是等t1 和 t2 都执行完后，再执行print(end-begin)输出时间差
t2.join()

end = time.time()
print(end-begin)  # 串行和 并行执行 并没有很大的速度提高

