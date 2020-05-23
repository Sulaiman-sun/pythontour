"""
save data or execute sql
"""
from . import sqlgen


class Executor:

    def __init__(self, con_pool):
        self.pool = con_pool

    def save(self, table, fields, values,
             step=1000, dup_update=False,
             keep_fields=("created_at",)
             ):
        for idx in range(0, len(values), step):
            batch = values[idx: idx + step]
            if not batch:
                return
            sql, val = sqlgen.insert_many(table=table,
                                          fields=fields,
                                          values=batch,
                                          dup_update=dup_update,
                                          keep_fields=keep_fields
                                          )
            self.execute(sql, val)

    def execute(self, sql, values, many=False):

        con = self.pool.connection()
        cur = con.cursor()
        try:
            if many:
                result = cur.executemany(sql, values)
            else:
                result = cur.execute(sql, values)
        except Exception as e:
            con.rollback()
            raise e
        else:
            con.commit()
        finally:
            cur.close()
            con.close()

        return result
