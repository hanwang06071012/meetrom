from flask import Flask
from flask import render_template
from pro import app
from pro.model.node_info  import NodeInfo

@app.route('/')
def show_default():
	print("=====================start ========================")
	NodeInfo.select("name")
	print("=====================  end ========================")
	return render_template('default.html')

@app.route('/fangwuchuzu')
def fangwuchuzu():
	return render_template('sub1/fangwuchuzu.html')


@app.route('/selectaddr')
def selectaddr():
	return render_template('selectaddr.html')
