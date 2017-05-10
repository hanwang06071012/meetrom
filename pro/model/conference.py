#!-*- coding:utf-8 -*-
#=======================================================
#作者：田川
#日期：2017-04-08
#功能：income数据表驱动
#更新：无
#备注：无
#=======================================================
from pro.model.bean import Bean

class Conference(Bean):
	_tbl = 'Conference'
	_id = 'ID'
	_cols = 'ID,Sqrzh,Sqrxm,Name,Didian,Duomeiti,Rongnarenshu,Hueiyizhuti,Shenqingzhuangtai,Shenpi,Shenqliyou,Shenqsjian'

	def __init__(self,ID,Sqrzh,Sqrxm,Name,Didian,Duomeiti,Rongnarenshu,Hueiyizhuti,Shenqingzhuangtai,Shenpi,Shenqliyou,Shenqsjian):
		self.ID = ID
		self.Sqrzh = Sqrzh
		self.Sqrxm = Sqrxm
		self.Name = Name
		self.Didian = Didian
		self.Duomeiti = Duomeiti
		self.Rongnarenshu = Rongnarenshu
		self.Hueiyizhuti = Hueiyizhuti
		self.Shenqingzhuangtai = Shenqingzhuangtai
		self.Shenpi = Shenpi
		self.Shenqliyou = Shenqliyou
		self.Shenqsjian = Shenqsjian
