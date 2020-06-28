#!/usr/bin/env python
# -*-coding:utf-8-*-
# date:2018/11/14
import cx_Oracle
#import MySQLdb
import time
import string
from DBUtils.PooledDB import PooledDB

pool = PooledDB(cx_Oracle, user = "alibaba", password = "alibaba", dsn = "test.db.alibaba.com:1525/testdb",mincached=2,maxcached=2,maxshared=2,maxconnections=2)

for i in range(1000):
    time.sleep(1)
    conn = pool.connection()
    cursor = conn.cursor()
    cursor.execute("""select * from dual""")
    result = cursor.fetchall();
    print  cursor.description
    conn.close();