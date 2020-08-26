import os
import sqlite3

class DB:
    def __init__(self):
        rootPath = os.path.abspath('.')
        dbFile = os.path.join(rootPath, 'config', 'data.set')

        self.tbName = ''

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
            '"udtime" TEXT,'
            '"isdel" integer DEFAULT 0);'
        )
        self.cur.execute(sql)
        sql = 'CREATE UNIQUE INDEX "alias" ON "tvg_info" ("alias");'
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

        sql = (
            'CREATE TABLE "log" ('
            '"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,'
            '"typ" text,'
            '"msg" text,'
            '"udtime" text'
            ');'
        )
        self.cur.execute(sql)

        self.conn.commit()

    def __getCol (self, tbName):
        sql = "PRAGMA table_info([%s])" % (tbName)
        tmp = self.query(sql)

        cols = []
        for item in tmp:
            cols.append(item[1])

        return cols

    def __fmtRst (self, tbName, data):
        cols = self.__getCol(self.tbName)
        result = []

        for item in data:
            tmp = {}
            i = 0
            for x in item:
                tmp[cols[i]] = x
                i += 1
            result.append(tmp)

        return result

    def __mkWhere (self, param):
        sql = ''
        for k, v in param.items():
            if k != 'where':
                sql += " AND `%s` = '%s'" % (k, v)
            else:
                sql += " AND %s" % (v)

        sql = 'WHERE ' + sql[5:]

        return sql

    def query (self, sql, values = ()):
        if self.connStat == False : return False

        self.cur.execute(sql, values)
        values = self.cur.fetchall()

        return values

    def exec (self, sql, values = ()):
        if self.connStat == False : return False

        try:
            self.cur.execute(sql, values)
            self.conn.commit()

            return True
        except:
            return False

    def getById (self, id):
        sql = 'SELECT * FROM %s WHERE id = %s' % (self.tbName, id)
        result = self.__fmtRst(self.tbName, self.query(sql))

        return result

    def getListByParam (self, param, typ):
        whereStr = self.__mkWhere(param)

        orderStr = ''
        if 'order' in typ:
            orderStr = 'ORDER BY %s' % (typ['order'])

        showStr = ''
        if 'limit' in typ:
            showStr = ' LIMIT %s' % (typ['limit'])
        elif 'p' in typ and 'ps' in typ:
            showStr = ' LIMIT %s, %s' % ((int(typ['p']) -1) * int(typ['ps']), int(typ['ps']))
        else:
            pass

        sql = "SELECT * FROM %s %s %s %s" % (self.tbName, whereStr, orderStr, showStr)
        result = self.__fmtRst(self.tbName, self.query(sql))    

        return result

    def addData (self, data):
        col = ''
        val = ''
        for k, v in data.items():
            col += ', "%s"' % (k)
            val += ', "%s"' % (v)

        sql = 'INSERT INTO %s (%s) VALUES (%s)' % (self.tbName, col[2:], val[2:])

        return self.exec(sql)

    def updateById (self, id, data):
        udStr = ''
        for k, v in data.items():
            udStr += ', `%s` = "%s"' % (k, v)

        sql = 'UPDATE %s SET %s WHERE id = %s' % (self.tbName, udStr[2:], id)

        return self.exec(sql)

    def delById (self, id):
        data = {'isdel': 1}

        return self.updateById (self, id, data)
