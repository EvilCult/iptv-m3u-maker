import pymysql

class DB:
    db = None
    table_name = ''

    def __init__(self, **kwargs):
        self.data = kwargs

    @classmethod
    def connect(cls, **config):
        cls.db = pymysql.connect(**config)

    @classmethod
    def close(cls):
        cls.db.close()

    @classmethod
    def execute(cls, query, params=None):
        with cls.db.cursor() as cursor:
            cursor.execute(query, params)
            result = cursor.fetchall()
        cls.db.commit()
        return result

    @classmethod
    def find(cls, val, key='id'):
        query = f'SELECT * FROM {cls.table_name} WHERE {key} = %s'
        result = cls.execute(query, (val,))
        if result:
            return cls(**(result[0]))
        return None

    @classmethod
    def where(cls, **kwargs):
        conditions = []
        values = []
        for key, value in kwargs.items():
            conditions.append(f'{key}=%s')
            values.append(value)
        query = f'SELECT * FROM {cls.table_name} WHERE {" AND ".join(conditions)}'
        result = cls.execute(query, values)
        return [cls(**row) for row in result]

    def save(self):
        if 'id' in self.data:
            query = f'UPDATE {self.table_name} SET {", ".join([f"{k}=%s" for k in self.data.keys()])} WHERE id = %s'
            params = list(self.data.values()) + [self.data['id']]
        else:
            query = f'INSERT INTO {self.table_name} ({", ".join(self.data.keys())}) VALUES ({", ".join(["%s" for _ in self.data.values()])})'
            params = list(self.data.values())
        self.execute(query, params)
        if 'id' not in self.data:
            self.data['id'] = self.db.insert_id()

    def delete(self):
        query = f'DELETE FROM {self.table_name} WHERE id = %s'
        self.execute(query, (self.data['id'],))
        self.data = {}

    @classmethod
    def __init_subclass__(cls, **config):
        super().__init_subclass__(**config)
        cls.connect(
            host='mysql',
            user='root',
            password='6Os9b0n7M4xN',
            database='test',
            cursorclass=pymysql.cursors.DictCursor
        )
