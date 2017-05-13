#!-*- coding:utf-8 -*-
#=======================================================
#作者：田川
#日期：2017-02-25
#功能：user数据表驱动
#更新：无
#备注：无
#=======================================================
from pro.model.bean import Bean

class Users(Bean):
	_tbl = 'Users'
	_id = 'ID'
	_cols = 'usersid,usersName,usersPass,usersRepass,usersPassQuestion,usersPassReply,usersTrueName,usersAddress,usersEmail,usersSpecialty,usersHuji,usersIDcard,usersCsrq,usersJiguan,usersAge,usersSex,createDate,usersPhone'

        def __init__(self,usersid,usersName,usersPass,usersRepass,usersPassQuestion,usersPassReply,usersTrueName,usersAddress,usersEmail,usersSpecialty,usersHuji,usersIDcard,usersCsrq,usersJiguan,usersAge,usersSex,createDate,usersPhone):
                self.usersid = usersid
                self.usersName = usersName
                self.usersPass = usersPass
                self.usersRepass = usersRepass
                self.usersPassQuestion = usersPassQuestion
                self.usersPassReply = usersPassReply
                self.usersTrueName = usersTrueName
                self.usersAddress = usersAddress
                self.usersEmail = usersEmail
                self.usersSpecialty = usersSpecialty
                self.usersHuji = usersHuji
                self.usersIDcard = usersIDcard
                self.usersCsrq = usersCsrq
                self.usersJiguan = usersJiguan
                self.usersAge = usersAge
                self.usersSex = usersSex
                self.createDate = createDate
                self.usersPhone = usersPhone
