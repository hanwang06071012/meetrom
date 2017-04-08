#!-*- coding:utf-8 -*-
#=======================================================
#作者：韩望
#日期：2017-02-25
#功能：estateagents数据表驱动
#更新：无
#备注：无
#=======================================================

class EstateAgents(Bean):
	_tbl = 'estate_agents'
	_id = 'id'
	_cols = 'id,name,level,time_modify,time_create'

	def __init__(self,id,name,level,time_modify,time_create):
		self.id =id
		self.name = name
		self.level = level
		self.time_modify = time_modify
		self.time_create = time_create
