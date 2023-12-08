import sqlite3

class DB:
    db = None
    table_name = ''

    def __init__(self, **kwargs):
        self.data = kwargs

    @classmethod
    def connect(cls, db_name):
        cls.db = sqlite3.connect(db_name, check_same_thread=False)

    @classmethod
    def close(cls):
        cls.db.close()

    @classmethod
    def execute(cls, query, params=None):
        with cls.db:
            cursor = cls.db.cursor()
            if params is not None:
                if isinstance(params, (tuple, list)):
                    cursor.execute(query, params)
                else:
                    cursor.execute(query, (params,))
            else:
                cursor.execute(query)
            result = cursor.fetchall()
        return result

    @classmethod
    def find(cls, val, key='id'):
        query = f'SELECT * FROM {cls.table_name} WHERE {key} = ?'
        data = cls.execute(query, (val,))
        return cls.fmtResult(data)

    @classmethod
    def where(cls, **kwargs):
        conditions = []
        values = []
        for key, value in kwargs.items():
            conditions.append(f'{key}=?')
            values.append(value)
        query = f'SELECT * FROM {cls.table_name} WHERE {" AND ".join(conditions)}'
        result = cls.execute(query, values)
        return cls.fmtResult(result)

    def save(self):
        if 'id' in self.data:
            query  = f'UPDATE {self.table_name} SET {", ".join([f"{k} = ?" for k in self.data.keys()])} WHERE id = ?'
            params = list(self.data.values()) + [self.data['id']]
        else:
            query  = f'INSERT INTO {self.table_name} ({", ".join(self.data.keys())}) VALUES ({", ".join(["?" for _ in self.data.values()])})'
            params = list(self.data.values())
        self.execute(query, params)
        if 'id' not in self.data:
            self.data['id'] = self.db.lastrowid

    def delete(self):
        query = f'DELETE FROM {self.table_name} WHERE id = ?'
        self.execute(query, (self.data['id'],))
        self.data = {}

    @classmethod
    def getColumns(cls):
        query = f'PRAGMA table_info({cls.table_name})'
        return cls.execute(query)

    @classmethod
    def fmtResult(cls, data):
        colName = cls.getColumns()
        result = []
        for row in data:
            tmp = {}
            for i in range(len(colName)):
                tmp[colName[i][1]] = row[i]
            result.append(tmp)
        return result

    @classmethod
    def __init_subclass__(cls, **config):
        super().__init_subclass__(**config)
        cls.connect(config.get('db_name', 'Data/config.db'))
