#-*- coding:utf-8 -*-
#============================================================
#作者：韩望
#日期：2017-04-02
#功能：初始化函数
#默认函数更新：无
#备注：无
#============================================================
from flask import Flask,session
from frame import const

#
def constset():
    session['master_city_id'] = const.DEFAULTCITYID

constset();