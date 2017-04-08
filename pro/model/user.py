#!-*- coding:utf-8 -*-
#=======================================================
#作者：韩望
#日期：2017-02-25
#功能：user数据表驱动
#更新：无
#备注：无
#=======================================================

class User(Bean):
	_tbl = 'user'
	_id = 'id'
	_cols = 'id,name,pwd,timecreate,timemodify'

	def __init__(self,id,name,pwd,timecreate,timemodify):
		self.id =id
		self.name = name
		self.pwd = pwd
		self.timecreate = timecreate
		self.timemodify = timemodify
