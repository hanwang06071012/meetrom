#-*- coding:utf-8 -*-
#============================================================
#作者：田川
#日期：2017-02-25
#功能：数据库的二次封装
#更新：无
#备注：无
#============================================================
from frame.multiDbStore  import db
class Bean(object):
	_tbl = ''
	_id = 'id'
	_cols = ''
	_dbname = 'meetrom'

	@classmethod
	def getdb(cls):
		return db

 	@classmethod
	def insert(cls, data=None):
		if not data:
			raise ValueError('argument data is invalid')
		db = cls.getdb()
		size = len(data)
		keys = data.keys()
		safe_keys = ['`%s`' % k for k in keys]
		sql = 'INSERT INTO `%s`(%s) VALUES(%s)' % (
			cls._tbl, ','.join(safe_keys), '%s' + ',%s' * (size - 1))
		last_id = db.insert(sql, [data[key] for key in keys])
		return last_id

	@classmethod
	def delete(cls,where=None,params=None):
		sql = 'DELETE FROM `%s`'% cls._tbl
		db = cls.getdb()
		if not where:
			return db.update(sql)
		sql += 'WHERE' + where
		return db.update(sql,params)

	@classmethod
	def delete_one(cls,pk=None):
		db = cls.getdb()
		sql = 'DELETE FROM `%S` WHERE %s == %%s' % (cls._tbl,cls._id)
		return db.update(sql,[pk])

	@classmethod
	def update(cls,clause=None,where='',params=None):
		db = cls.getdb()
		sql = 'UPDATE `%s` SET %s' %(cls._tbl,clause)
		return db.update(sql,params)

	@classmethod
	def update_dict(cls,data=None,where='',params=None):
		if not data:
			raise ValueError('argument data is invalid')
		db = cls.getdb()
		size = len(data)
		keys = data.keys()
		safe_keys = ['`%s`' % k for k in keys]
		values = [data[key] for key in keys]
		arr = ['%s=%%s'% key for key in safe_keys]
		if not where:
			return cls.update(','.join(arr),values)
		else:
			values.extend(params)
			return cls.update(', '.join(arr) + 'WHERE' + where,values)

 	@classmethod
	def select(cls, cols=None, where=None, params=None, order=None, limit=None, page=None, offset=None):
		if cols is None:
			cols = cls._cols

		if params is None:
			params = []

		db = cls.getdb()
		sql = 'SELECT %s FROM `%s`' % (cols, cls._tbl)

		if where:
			sql = '%s WHERE %s' % (sql, where)

		if order:
			sql = '%s ORDER BY %s' % (sql, order)

		if limit is not None:
			sql = '%s LIMIT %s' % (sql, limit)

		if offset is not None:
			sql = '%s OFFSET %s' % (sql, offset)

		if page is not None:
			offset = (int(page) - 1) * int(limit)
			if offset < 0:
				offset = 0
			sql = '%s OFFSET %s' % (sql, offset)
		print("sql=%s" % sql )

		return db.query_all(sql, params)

	@classmethod
	def select_vs(cls,where=None,params=None,order=None,limit=None,page=None,offset=None):
		rows = cls.select(where=where,params=params,order=order,limit=limit,page=page,offset=offset)
		return [cls(*row) for row in rows]

	@classmethod
	def read(cls,where=None,params=None):
		vs = cls.select_vs(where=where,params=params)
		if vs:
			return vs[0]
		else:
			return None

	@classmethod
	def get(cls,id_val):
		if not id_val:
			return None
		return cls.read('%s = %s'% cls._id,[id_val])

	@classmethod
	def column(cls,col=None,where=None,params=None,order=None,limit=None,page=None,offset=None):
		rows = cls.select(col,where,params,order,limit,page,offset)
		return [row[0] for row in rows]

	@classmethod
	def total(cls,where=None,params=None):
		db=cls.getdb()
		if not where:
			ret=db.query_column(sql)
			return ret[0]
		sql += 'WHERE' + where
		ret = db.query_column(sql,params)
		return ret[0]

	@classmethod
	def exists(cls,where=None,params=None):
		return cls.total(where,params) > 0
