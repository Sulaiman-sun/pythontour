"""
generate sql for insert
"""
def get_duplicate(fields, keep_fields):
    update_pattern = ','.join([f"`{f}`=VALUES(`{f}`)"
                               for f in fields
                               if f not in keep_fields]
                              )
    return f"ON DUPLICATE KEY UPDATE {update_pattern}"


def get_values(fields, values=None):
    val_pat = ','.join([f"({','.join(['%s'] * len(fields))})"] * len(values))
    val = tuple([v[f] for v in values for f in fields])
    return val_pat, val


def insert_many(table, fields, values, dup_update=False, keep_fields=("created_at",)):
    """

    :param table:
    :param fields:
    :param values: 待插入`table`的多条数据，每条数据是一个字典对象。eg. [{"f1": 2}, {"f1": 3}, ...,]
    :param dup_update: 主键冲突时是否更新数据
    :param keep_fields: 主键冲突更新数据时保留原值的字段，eg. created_at
    :return:
    >> table = 'demo'
    >> fields = ['f1', 'f2']
    >> values = [
        {"f1": 1, "f2": 1},
        {"f1": 2, "f2": 2},

    ]
    >> sql, val = sqlgen.insert_many(table=table, fields=fields, values=values, dup_update=True)
    >> sql
    INSERT INTO `demo` (`f1`, `f2`) VALUES (%s,%s),(%s,%s) ON \
    DUPLICATE KEY UPDATE `f1`=VALUES(`f1`),`f2`=VALUES(`f2`)
    >> values
    (1, 1, 2, 2)

    """
    fstr = '`, `'.join(fields)
    if dup_update:
        on_duplicate = get_duplicate(fields, keep_fields)
    else:
        on_duplicate = ""
    val_pat, val = get_values(fields=fields, values=values)
    sql = f"""INSERT INTO `{table}` (`{fstr}`) VALUES {val_pat} {on_duplicate}"""
    return sql, val
