# coding=utf-8
"""
根据数据表生成对应的实体
董新强
日期:2016-02-15
"""
import os
import pymysql


from config.secure import MySqlConfig
MySqlConfig = MySqlConfig.get('work_4433_setting')
conn = pymysql.connect(host=MySqlConfig['host'], port=MySqlConfig['port'], user=MySqlConfig['user'],
                       passwd=MySqlConfig['password'], db='information_schema',
                       charset='utf8')
_tables = {}
_dir = ''

_datatable = MySqlConfig['db']


def get_tables():
    '''
    获取数据库中所有的表
    '''
    try:
        cur = conn.cursor()
        cur.execute(
            "select TABLE_NAME, TABLE_COMMENT from TABLES WHERE TABLE_SCHEMA='" + _datatable + "' order by TABLE_NAME")
        print('表名:')
        for v in cur:
            _tables[v[0]] = v[1]
            print(v[0])
        cur.close()

        print('请输入需要生成的表,输入-q退出')
        tb = input('')
        while tb != '-q':
            cur = conn.cursor()

            if not tb or not tb in _tables:
                print('表名错误,请重新输入')
            else:

                sql = "select COLUMN_NAME,ORDINAL_POSITION,IS_NULLABLE,DATA_TYPE,COLUMN_TYPE,COLUMN_KEY,COLUMN_COMMENT from columns  where table_schema='" + _datatable + "' and TABLE_NAME ='" + tb + "'"
                cur.execute(sql)
                write_to_file(cur, tb, _tables[tb])
                cur.close()
                print('完成表到实体的转换')
            tb = input('')
        print('退出')
    except:
        print('异常=>')
    finally:
        conn.close()


def write_to_file(row, tb, tbdesc):
    path = _dir + r'/' + tb + '.py'

    f = open(path, 'w', encoding='utf-8')
    f.write('# coding=utf-8')
    f.write('\n')
    f.write('from datetime import datetime')
    f.write('\n')
    f.write('import time')
    f.write('\n')
    f.write('from app.models.base import db')
    f.write('\n')
    f.write(
        'from sqlalchemy import Column, Integer, String, DateTime, Numeric, Boolean, SMALLINT, BigInteger, Float, TEXT, Date')
    f.write('\n')
    f.write('\n')
    f.write('\n')
    f.write('class ')
    f.write(tb.title().replace('_', ""))
    f.write('(db.Model):')
    f.write('\n')
    f.write("    \"\"\"\n")
    f.write('    模型(表)备注:\n')
    f.write("    " + tbdesc)
    f.write('\n')
    f.write("    \"\"\"")
    f.write('\n')
    f.write("    __tablename__ = '")
    f.write(tb + "'")
    f.write('\n\n')

    reprs = []
    keys_list = []
    for v in row:
        item = '    %s = Column(%s' % (v[0], getType(v[4]),)
        if v[5] == 'PRI':
            item += ', primary_key=True'
            comment = "    '''   " + v[6] + "   '''"
        elif v[2] == 'NO':
            item += ', nullable=False'
            comment = "    '''   " + v[6] + "   '''"
        else:
            comment = "    '''   " + v[6] + "   '''"
        keys_list.append(v[0])
        reprs.append("%s='{self.%s}'" % (v[0], v[0]))
        item += ')'
        f.write(comment)
        f.write('\n')
        f.write(item)
        f.write('\n\n')

    '''   -----------------------写入文件--------------------------------------   #endregion '''
    f.close()


def getType(tp):
    t = tp.split('(')
    if len(t) > 1:
        t[1:2] = t[1].split(')')
    if t[0] == 'varchar':
        return 'String(%s)' % t[1]
    if t[0] == 'datetime':
        return 'DateTime(), default=datetime.now'
    if t[0] == 'int':
        return "Integer()"
    if t[0] == 'decimal':
        return 'Numeric(' + (t[1]) + ')'
    if t[0] == 'char':
        return 'String(%s)' % t[1]
    if t[0] == 'bit':
        return 'Boolean()'
    if t[0] == 'bigint':
        return 'BigInteger()'
    if t[0] == 'varbinary':
        return 'Binary(%s)' % t[1]
    if t[0] == 'text':
        return 'TEXT()'
    if t[0] == 'double':
        return 'Float'
    if t[0] == 'smallint':
        return 'SMALLINT'
    return tp


if __name__ == "__main__":
    _dir = r"E:\项目\flask_4433\app\models"
    if not os.path.exists(_dir):
        os.mkdir(_dir)
    print('存储路径为=>', _dir)
    get_tables()
