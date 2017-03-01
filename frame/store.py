#-*- coding:utf-8 -*-
#=======================================================
#作者：韩望
#日期：2017-02-19
#功能：数据库驱动一次封装
#更新：无
#备注：无
#=======================================================

import MySQLdb,logging
import config

def connect_db(cfg):
	try:
		conn = MySQLdb.connect(
				host = cfg.BOUNTY_DB_HOST,
				port = cfg.BOUNTY_DB_PORT,
				user = cfg.BOUNT_DB_USER,
				passwd = cfg.BOUNTY_DB_PASSWD,
				db = cfg.BOUNTY_DB_NAME,
				use_unicode=True,
				charset="utf8",)
		return conn
	except Exception,e:
		logging.getLogger().critical('connect db: %s '% e)
		return None

class DB(object):
	def __init__(self,cfg):
		self.config = cfg
		self.conn = None
	def get_conn(self):
		if self.conn is None:
			self.conn = connect_db(self.config)
		return self.conn
	def execute(self,*a,**kw):
		cursor = kw.pop('cursor',None)
		try:
			cursor = cursor or self.get_conn.cursor()
			cursor.execute(*a,**kw)
		except(AttributeError,MySQLdb.operationalError):
			self.conn and self.conn.close()
			self.conn = None
			cursor = self.get_conn().cursor()
			cursor.execute(*a,**kw)
		return cursor
	def insert(self,*a,**kw):
		cursor = None
		try:
			cursor = self.execute(*a,**kw)
			row_id = cursor.lastrowid
			self.commit()
			return row_id
		except MySQLdb.InterityError:
			self.rollback()
		finally:
			cursor and cursor.close()
	def update(self,*a,**kw):
		cursor = None
		try:
			cursor = self.execute(*a,**kw)
			self.commit()
			row_count = cursor.rowcount
		except MySQLdb.IntegrityError():
			self.rollback()
		finally:
			cursor and cursor.close()
	def query_all(self,*a,**kw):
		cursor = None
		try:
			cursor = self.execute(*a,**kw)
			self.commit()
			return cursor.fetchall()
		finally:
			cursor and cursor.close()
	def query_one(self,*a,**kw):
		rows=self.query_all(*a,**kw)
		if rows:
			return rows[0]
		else:
			return None
	def query_column(self,*a,**kw):
		rows = self.query_all(*a,**kw)
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
db = DB(config)
