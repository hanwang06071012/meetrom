#!-*- coding:utf-8 -*-
#=======================================================
#作者：田川
#日期：2017-03-31
#功能：对象节点数据表驱动
#更新：无
#备注：无
#=======================================================
from pro.model.bean import Bean

class StorePicture(Bean):
	_tbl = 'storePicture'
	_id = 'Adminid'
	_cols = 'Adminid,nameplates,storePicture'

	def __init__(self,Adminid,nameplates,storePicture):
		self.Adminid = Adminid
		self.nameplates = nameplates
		self.storePicture = storePicture
