import os
import sqlite3

class DB:
    def __init__(self):
        rootPath = os.path.abspath('.')
        dbFile = os.path.join(rootPath, 'config', 'data.set')

        if self.__connect(dbFile) == False:
            self.connStat = False
        else :
            self.connStat = True
            print('need')
            self.__chkTable()

    def __del__(self):
        if self.connStat == True :
            try:
                self.__disConn()
            except:
                pass

    def __connect (self, path):
        try:
            self.conn = sqlite3.connect(path, check_same_thread = False)
            self.cur = self.conn.cursor()
            return True
        except:
            return False

    def __disConn (self):
        if self.connStat == False : return False

        self.cur.close()
        self.conn.close()

    def __chkTable (self):
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

    def __create (self):
        if self.connStat == False : return False

        sql = (
            'CREATE TABLE "tvg_info" ('
            '"id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,'
            '"num" INTEGER DEFAULT 99999,'
            '"title" TEXT,'
            '"alias" TEXT,'
            '"group" TEXT,'
            '"icon" TEXT,'
            '"isdel" integer DEFAULT 0);'
        )
        self.cur.execute(sql)

        sql = (
            'CREATE TABLE "setting" ('
            '"id" integer PRIMARY KEY AUTOINCREMENT,'
            '"version" text,'
            '"bot" integer(500)'
            ');'
        )
        self.cur.execute(sql)
        sql = 'INSERT INTO "setting" ("version", "bot" ) VALUES ("2.0.0", 0)'
        self.cur.execute(sql)

        self.conn.commit()

    def query (self, sql):
        if self.connStat == False : return False

        self.cur.execute(sql)
        values = self.cur.fetchall()

        return values

    def exec (self, sql):
        if self.connStat == False : return False

        try:
            self.cur.execute(sql)
            self.conn.commit()

            return True
        except:
            return False
