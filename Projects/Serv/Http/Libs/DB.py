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
    def find(cls, val, key='id', force=False):
        if not force:
            query = f'SELECT * FROM {cls.table_name} WHERE {key} = ? AND isdel = 0'
        else:
            query = f'SELECT * FROM {cls.table_name} WHERE {key} = ?'
        data = cls.execute(query, (val,))
        return cls.fmtResult(data)

    @classmethod
    def where(cls, **kwargs):
        query = f'SELECT * FROM {cls.table_name}'

        conditions = []
        values = []
        for key, value in kwargs.items():
            if key == 'limit' or key == 'offset':
                continue
            conditions.append(f'{key}=?')
            values.append(value)
        if len(conditions) > 0:
            query += f' WHERE {" AND ".join(conditions)}'

        if 'limit' in kwargs:
            query += f' LIMIT {kwargs["limit"]}'
        if 'offset' in kwargs:
            query += f' OFFSET {kwargs["offset"]}'

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
            self.data['id'] = self.execute('SELECT last_insert_rowid()')[0][0]

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

    @classmethod
    def __del_subclass__(cls):
        cls.close()
        super().__del_subclass__()

    @classmethod
    def counts(cls, **kwargs):
        query = f'SELECT COUNT(*) FROM {cls.table_name}'

        conditions = []
        values = []
        for key, value in kwargs.items():
            if key == 'limit' or key == 'offset':
                continue
            conditions.append(f'{key}=?')
            values.append(value)
        if len(conditions) > 0:
            query += f' WHERE {" AND ".join(conditions)}'

        return cls.execute(query)[0][0]

    @classmethod
    def select(cls, page=1, limit=20, type='normal'):
        if type == 'normal':
            query = f'SELECT * FROM {cls.table_name} where isdel = 0 LIMIT ? OFFSET ?'
        elif type == 'del':
            query = f'SELECT * FROM {cls.table_name} where isdel = 1 LIMIT ? OFFSET ?'
        else:
            query = f'SELECT * FROM {cls.table_name} LIMIT ? OFFSET ?'
        return cls.execute(query, (limit, (int(page) - 1) * int(limit)))

    @classmethod
    def selectAll(cls, force=False):
        if not force:
            query = f'SELECT * FROM {cls.table_name} where isdel = 0'
        else:
            query = f'SELECT * FROM {cls.table_name}'
        return cls.execute(query)
