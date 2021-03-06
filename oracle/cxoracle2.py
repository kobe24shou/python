#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:ls

from __future__ import print_function
import cx_Oracle
import os


oh="D:\instantclient_12_2"
os.environ["ORACLE_HOME"]=oh
os.environ["PATH"] = oh+os.pathsep+os.environ["PATH"]
os.environ["NLS_LANG"] = "AMERICAN_AMERICA.AL32UTF8"


def printConnectionAttr(connection):
    if connection is not None and isinstance(connection,cx_Oracle.Connection):
        print("Data Source Name  = ",connection.dsn)
        a="true" if connection.autocommit==1 else "False"
        print("Autocommit         = ",a)
        print("Session Edition    = ",connection.edition)
        print("Encoding           = ",connection.encoding)
        print("National Encoding  = ",connection.nencoding)
        print("Logical Tx Id      = ",connection.ltxid)
        print("Server version     = ",connection.version)

def connectToOracle(url, username, password, mode=None):
    try:
        if mode is not None:
            connection = cx_Oracle.Connection (user=username, password=password, dsn=url, mode=mode)
        else:
            connection = cx_Oracle.Connection (user=username, password=password, dsn=url)
    except cx_Oracle.DatabaseError as ex:
        raise
    return connection





# main

if __name__ == '__main__':
    c=cx_Oracle.Connection
    try:
        c=connectToOracle("192.168.10.228:1521/test11g","scott","oracle")
      # c=connectToOracle("192.168.10.222:1521/orcl","rspay","rspay",mode=cx_Oracle.SYSDBA)
    except cx_Oracle.DatabaseError as ex:
        err, =ex.args
        print("Error code    = ",err.code)
        print("Error Message = ",err.message)
        os._exit(1)
    printConnectionAttr(c)
    c.close()
