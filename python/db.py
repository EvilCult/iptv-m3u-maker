
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3
import getpass
import os
import time

class DataBase (object) :

    def __init__ (self) :
        self.dbAddress = os.path.dirname(os.path.abspath(__file__)).replace('python', 'database')

        self.table = 'lists'

        if self.connect() == False:
            self.connStat = False
        else :
            self.connStat = True

    def __del__ (self) :
        if self.connStat == True :
            self.disConn()

    def connect (self) :
        try:
            if not os.path.exists(self.dbAddress) :
                os.makedirs(self.dbAddress)
            self.dbAddress += 'db.sqlite3'
            self.conn = sqlite3.connect(self.dbAddress)
            self.cur = self.conn.cursor()
            return True
        except :
            return False

    def create (self) :
        if self.connStat == False : return False

        sql = 'create table ' + self.table + ' (id integer PRIMARY KEY autoincrement, title text, quality text, url text, level integer, cros integer,  enable integer, online integer, delay integer, udTime text)'
        self.cur.execute(sql)

    def query (self, sql, reTry = 3) :
        if self.connStat == False : return False

        try:
            self.cur.execute(sql)
            values = self.cur.fetchall()

            return values
        except:
            if reTry > 0 :
                time.sleep(1)
                reTry = reTry - 1
                return self.query(sql, reTry)

    def execute (self, sql) :
        try :
            if self.connStat == False : return False
            self.cur.execute(sql)
            return True
        except :
            return False

    def insert (self, data, reTry = 3):
        if self.connStat == False : return False

        keyList = []
        valList = []
        for k, v in data.items():
            keyList.append(k)
            valList.append(str(v).replace('"','\"').replace("'","''"))

        sql = "insert into " + self.table + " (`" + '`, `'.join(keyList) + "`) values ('" + "', '".join(valList) + "')"
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except:
            if reTry > 0 :
                time.sleep(1)
                reTry = reTry - 1
                self.insert(data, reTry)

    def edit (self, id, data, reTry = 3):
        if self.connStat == False : return False

        param = ''
        for k, v in data.items():
            param = param + ", `%s` = '%s'" %(k, str(v).replace('"','\"').replace("'","''"))

        param = param[1:]

        sql = "update " + self.table + " set %s WHERE id = %s" % (param, id)
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except:
            if reTry > 0 :
                time.sleep(1)
                reTry = reTry - 1
                self.edit(id, data, reTry)


    def disConn (self) :
        if self.connStat == False : return False

        self.cur.close()
        self.conn.close()

    def chkTable (self) :
        if self.connStat == False : return False

        sql = "SELECT tbl_name FROM sqlite_master WHERE type='table'"
        tableStat = False

        self.cur.execute(sql)
        values = self.cur.fetchall()

        for x in values:
            if self.table in x :
                tableStat = True

        if tableStat == False :
            self.create()

