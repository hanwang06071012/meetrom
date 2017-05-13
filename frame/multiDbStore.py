#-*- coding:utf-8 -*-
#=======================================================
#作者：田川
#日期：2017-02-19
#功能：数据库驱动一次封装
#更新：无
#备注：无
#=======================================================

import MySQLdb
from frame import config

def connect_db(host, port, user, password, db):
    try:
        conn = MySQLdb.connect(
            host=host,
            port=port,
            user=user,
            passwd=password,
            db=db,
            use_unicode=True,
            charset="utf8")
        return conn
    except Exception, e:
        print "Fatal: connect db fail:%s" % e
        return None

class Multi_DB(object):

    def __init__(self, host, port, user, password, db):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.conn = None

    def connect(self):
        if not self.conn:
            self.conn = connect_db(self.host, self.port, self.user, self.password, self.db)
        return self.conn

    def get_conn(self):
        if self.conn is None:
            self.conn = connect_db(self.host, self.port, self.user, self.password, self.db)
        return self.conn

    def execute(self, *a, **kw):
        cursor = kw.pop('cursor', None)
        try:
            cursor = cursor or self.get_conn().cursor()
            cursor.execute(*a, **kw)
        except (AttributeError, MySQLdb.OperationalError):
            self.conn and self.conn.close()
            self.conn = None
            cursor = self.get_conn().cursor()
            cursor.execute(*a, **kw)
        return cursor

    # insert one record in a transaction
    # return last id
    def insert(self, *a, **kw):
        cursor = None
        try:
            cursor = self.execute(*a, **kw)
            row_id = cursor.lastrowid
            self.commit()
            return row_id
        except MySQLdb.IntegrityError:
            self.rollback()
        finally:
            cursor and cursor.close()

    # update in a transaction
    # return affected row count
    def update(self, *a, **kw):
        cursor = None
        try:
            cursor = self.execute(*a, **kw)
            self.commit()
            row_count = cursor.rowcount
            return row_count
        except MySQLdb.IntegrityError:
            self.rollback()
        finally:
            cursor and cursor.close()

    def query_all(self, *a, **kw):
        cursor = None
        # print "query_all *a=[%s], **kw=[%s]\n" % (a, kw)
        try:
            print(*a)
            print(**kw)
            cursor = self.execute(*a, **kw)
            self.commit() 
            return cursor.fetchall()
        finally:
            cursor and cursor.close()

    def query_one(self, *a, **kw):
        rows = self.query_all(*a, **kw)
        if rows:
            return rows[0]
        else:
            return None

    def query_column(self, *a, **kw):
        rows = self.query_all(*a, **kw)
        if rows:
            return [row[0] for row in rows]
        else:
            return []

    def commit(self):
        if self.conn:
            try:
                self.conn.commit()
            except MySQLdb.OperationalError:
                self.conn = None

    def rollback(self):
        if self.conn:
            try:
                self.conn.rollback()
            except MySQLdb.OperationalError:
                self.conn = None

db = Multi_DB(
		config.MEETROM_DB_HOST,
		config.MEETROM_DB_PORT,
		config.MEETROM_DB_USER,
		config.MEETROM_DB_PASSWD,
		config.MEETROM_DB_NAME)
