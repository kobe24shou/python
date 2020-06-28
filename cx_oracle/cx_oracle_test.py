#!/usr/bin/env python
# -*-coding:utf-8-*-
# date:2018/11/14


import cx_Oracle
import MySQLdb
import time
import string

class PooledConnection:

    def __init__(self, maxconnections, connstr,dbtype):
        from Queue import Queue
        self._pool = Queue(maxconnections) # create the queue
        self.connstr = connstr
        self.dbtype=dbtype
        self.maxconnections=maxconnections
        try:
            for i in range(maxconnections):
                self.fillConnection(self.CreateConnection(connstr,dbtype))
        except Exception,e:
            raise e

    def fillConnection(self,conn):
        try:
            self._pool.put(conn)

        except Exception,e:
            raise "fillConnection error:"+str(e)

    def returnConnection(self, conn):
        try:
            self._pool.put(conn)
        except Exception,e:
            raise "returnConnection error:"+str(e)

    def getConnection(self):
        try:
            return self._pool.get()
        except Exception,e:
            raise "getConnection error:"+str(e)

    def ColseConnection(self,conn):
        try:
            self._pool.get().close()
            self.fillConnection(self.CreateConnection(connstr,dbtype))
        except Exception,e:
            raise "CloseConnection error:"+str(e)

    def CreateConnection(self,connstr,dbtype):
        if dbtype=='oracle':
            try:
                db_conn = connstr.split("#");
                connection=cx_Oracle.connect(db_conn[0],db_conn[1],db_conn[2],threaded=True)
                connection.clientinfo = 'datasync connection pool from datasync.py'
                connection.ping()
                return connection
            except Exception,e:
                raise 'conn targetdb datasource Excepts,%s!!!(%s).'%(db_conn[2],str(e))
                return None
        elif dbtype=='mysql':
            try:
                db_conn = connstr.split("#");
                #conndb=MySQLdb.connect(db=conf.mydb,host=conf.dbip,user=conf.myuser,passwd=conf.mypasswd);
                conndb=MySQLdb.connect(user=db_conn[0],passwd=db_conn[1],host=db_conn[2],port=string.atoi(db_conn[3]),db=db_conn[4]);
                conndb.clientinfo = 'datasync connection pool from datasync.py';
                conndb.ping();
            except Exception, e:
                raise 'conn targetdb datasource Excepts,%s!!!(%s).'%(db_conn[2],str(e))
                return None

