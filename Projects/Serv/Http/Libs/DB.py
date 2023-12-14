import sqlite3

class DB:
    db = None
    table_name = ''

    def __init__(self, **kwargs):
        pass

    @classmethod
    def __init_subclass__(cls, **config):
        super().__init_subclass__(**config)
        cls.connect(config.get('db_name', 'Data/config.db'))

    @classmethod
    def __del_subclass__(cls):
        cls.close()
        super().__del_subclass__()

    @classmethod
    def connect(cls, db_name):
        cls.db = sqlite3.connect(db_name, check_same_thread=False)

    @classmethod
    def close(cls):
        cls.db.close()

    @classmethod
    def save(cls, **kwargs):
        data = kwargs
        if 'id' in data:
            query  = f'UPDATE {cls.table_name} SET {", ".join([f"{k} = ?" for k in data.keys()])} WHERE id = ?'
            params = list(data.values()) + [data['id']]
        else:
            query  = f'INSERT INTO {cls.table_name} ({", ".join(data.keys())}) VALUES ({", ".join(["?" for _ in data.values()])})'
            params = list(data.values())
        cls.execute(query, params)
        if 'id' not in data:
            return cls.execute('SELECT last_insert_rowid()')[0][0]

    @classmethod
    def remove(cls, id):
        query = f'DELETE FROM {cls.table_name} WHERE id = ?'
        cls.execute(query, (id,))

    @classmethod
    def select(cls, **kwargs):
        cls.query = f"SELECT * FROM {cls.table_name}"
        cls.values = []

        conditions = []
        values = []
        for key, value in kwargs.items():
            if 'LIKE' not in str(key):
                conditions.append(f'{key}=?')
                values.append(value)
            else:
                conditions.append(f'{key} ?')
                values.append('%' + value + '%')
        if len(conditions) > 0:
            cls.query += f' WHERE {" AND ".join(conditions)}'
            cls.values += values

        return cls

    @classmethod
    def limit(cls, limit):
        cls.query += f" LIMIT ?"
        cls.values.append(limit)
        return cls

    @classmethod
    def page(cls, page, limit):
        cls.query += f" LIMIT ? OFFSET ?"
        cls.values.append(limit)
        cls.values.append((int(page) - 1) * int(limit))
        return cls

    @classmethod
    def offset(cls, offset):
        cls.query += f" OFFSET ?"
        cls.values.append(offset)
        return cls

    @classmethod
    def orderBy(cls, orderBy):
        cls.query += f" ORDER BY {orderBy}"
        return cls

    @classmethod
    def groupBy(cls, groupBy):
        cls.query += f" GROUP BY {groupBy}"
        return cls

    @classmethod
    def counts(cls, **kwargs):
        cls.query = f"SELECT COUNT(*) FROM {cls.table_name}"
        cls.values = []

        conditions = []
        values = []
        for key, value in kwargs.items():
            conditions.append(f'{key}=?')
            values.append(value)
        if len(conditions) > 0:
            cls.query += f' WHERE {" AND ".join(conditions)}'
            cls.values += values

        return cls

    @classmethod
    def fetch(cls):
        if 'COUNT(*)' not in cls.query:
            return cls.fmtResult(cls.execute(cls.query, cls.values))
        else:
            return cls.execute(cls.query, cls.values)[0][0]

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
