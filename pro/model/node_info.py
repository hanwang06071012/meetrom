#!-*- coding:utf-8 -*-
#=======================================================
#作者：韩望
#日期：2017-03-31
#功能：对象节点数据表驱动
#更新：无
#备注：无
#=======================================================
from pro.model.bean import Bean

class NodeInfo(Bean):
	_tbl = 'node_info'
	_id = 'id'
	_cols = ''

	def __init__(self,id,node_id,parent_id,name,link_name,addris,timecreate,timemodify):
		self.id =id
		self.node_id = node_id
		self.parent_id = parent_id
		self.name = name
		self.link_name = link_name
		self.addris = addris
		self.timecreate = timecreate
		self.timemodify = timemodify
