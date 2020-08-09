import os
import sqlite3

class DB:
    def __init__(self):
        rootPath = os.path.abspath('.')
        dbFile = os.path.join(rootPath, 'data.set')

        if self.__connect(dbFile) == False:
            self.connStat = False
        else :
            self.connStat = True
            self.__chkTable()

    def __del__(self):
        if self.connStat == True :
            try:
                self.__disConn()
            except:
                pass

    def __connect (self, path) :
        try:
            self.conn = sqlite3.connect(path, check_same_thread = False)
            self.cur = self.conn.cursor()
            return True
        except:
            return False

    def __disConn (self) :
        if self.connStat == False : return False

        self.cur.close()
        self.conn.close()

    def __chkTable (self) :
        if self.connStat == False : return False

        sql = "SELECT tbl_name FROM sqlite_master WHERE type='table'"
        tableStat = False

        self.cur.execute(sql)
        values = self.cur.fetchall()

        for x in values:
            if 'setting' in x :
                tableStat = True

        if tableStat == False :
            self.__create()

    def __create (self) :
        if self.connStat == False : return False

        sql = 'create table setting (id integer PRIMARY KEY autoincrement, bdc text, path varchar(500), ariarpc varchar(500), ariapath varchar(500), udrate int(1), udtime varchar(100))'
        
        self.cur.execute(sql);
        self.conn.commit()

