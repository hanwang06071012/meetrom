#-*- coding:utf-8 -*-
#=======================================================
#作者：韩望
#日期：2017-02-19
#功能：数据库驱动
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
