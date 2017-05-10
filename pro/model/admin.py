#!-*- coding:utf-8 -*-
#=======================================================
#作者：田川
#日期：2017-04-08
#功能：estateagents数据表驱动
#更新：无
#备注：无
#=======================================================
from pro.model.bean import Bean

class Admin(Bean):
	_tbl = 'Admin'
	_id = 'Adminid'
	_cols = 'Adminid,AdminName,AdminPass,AdminRepass,AdminPassQuestion,AdminPassReply,AdminTrueName,AdminAddress,AdminEmail,AdminSpecialty,AdminHuji,AdminIDcard,AdminCsrq,AdminJiguan,AdminAge,AdminSex,AdminPhone'
        def __init__(self,Adminid,AdminName,AdminPass,AdminRepass,AdminPassQuestion,AdminPassReply,AdminTrueName,AdminAddress,AdminEmail,AdminSpecialty,AdminHuji,AdminIDcard,AdminCsrq,AdminJiguan,AdminAge,AdminSex,AdminPhone):
                self.Adminid = Adminid
                self.AdminName = AdminName
                self.AdminPass = AdminPass
                self.AdminRepass = AdminRepass
                self.AdminPassQuestion = AdminPassQuestion
                self.AdminPassReply = AdminPassReply
                self.AdminTrueName = AdminTrueName
                self.AdminAddress = AdminAddress
                self.AdminEmail = AdminEmail
                self.AdminSpecialty = AdminSpecialty
                self.AdminHuji = AdminHuji
                self.AdminIDcard = AdminIDcard
                self.AdminCsrq = AdminCsrq
                self.AdminJiguan = AdminJiguan
                self.AdminAge = AdminAge
                self.AdminSex = AdminSex
                self.AdminPhone = AdminPhone
