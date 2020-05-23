import random
import os

from mysql import sqlgen
from mysql.connector import ConnectionPool
from mysql.executor import Executor


def test_sql():
    table = 'demo'
    fields = ['f1', 'f2']
    values = [
        {"f1": 1, "f2": 1},
        {"f1": 2, "f2": 2},

    ]
    sql, val = sqlgen.insert_many(table=table, fields=fields, values=values, dup_update=True)
    print(sql)
    print(val)


def produce_data(nums):
    return [
        {
            "uid": 10000 + num,
            "name": f"name{num}",
            "age": random.randint(10, 150)
        } for num in range(nums)
    ]


def test_insert():
    db_name = os.environ['DB_NAME']
    pwd = os.environ['DB_PWD']
    table = 'demo'
    fields = ['uid', 'name', 'age']
    connector = ConnectionPool(db=db_name, passwd=pwd)
    executor = Executor(con_pool=connector)
    values = produce_data(100)
    executor.save(table=table, fields=fields, values=values, dup_update=True)


if __name__ == '__main__':
    test_sql()
    test_insert()
