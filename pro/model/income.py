#!-*- coding:utf-8 -*-
#=======================================================
#作者：韩望
#日期：2017-04-08
#功能：income数据表驱动
#更新：无
#备注：无
#=======================================================
from pro.model.bean import Bean

class Income(Bean):
	_tbl = 'income'
	_id = 'id'
	_cols = 'id,city_type,frist_levle,second_level,thrid_level,forth_level,fifth_level,sixth_level,seventh_level,eigth_level,time_modify,time_create'

	def __init__(self,id,city_type,frist_level,second_level,thrid_level,forth_level,fifth_level,sixth_level,seventh_level,eigth_level,time_modify,time_create):
		self.id=id
		self.city_type=city_type
		self.frist_level=frist_level
		self.second_level=second_level
		self.thrid_level=thrid_level
		self.forth_level=forth_level
		self.fifth_level=fifth_level
		self.sixth_level=sixth_level
		self.seventh_level=seventh_level
		self.eigth_level=eigth_level
		self.time_modify=time_modify
		self.time_create=time_create
