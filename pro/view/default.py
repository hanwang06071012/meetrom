#-*- coding:utf-8 -*-
#============================================================
#作者：韩望
#日期：2017-04-02
#功能：数据库的二次封装
#更新：无
#备注：无
#============================================================
from flask import Flask,session
from flask import render_template
from pro import app
from pro.model.node_info  import NodeInfo
import json

@app.route('/')
def show_default():
	session['node_name'] = json.dumps("北京")
	print("=====================start ========================")
	str_sel = NodeInfo.select(cols="name")
	print str_sel
	print("=====================  end ========================")
	return render_template('default.html',**locals())

@app.route('/fangwuchuzu')
def fangwuchuzu():
	return render_template('sub1/fangwuchuzu.html')


@app.route('/selectaddr')
def selectaddr():
	return render_template('selectaddr.html')
