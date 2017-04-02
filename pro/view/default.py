from flask import Flask,session
from flask import render_template
from pro import app
from pro.model.node_info  import NodeInfo

@app.route('/')
def show_default():
	session['node_name'] = "beijing"
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
