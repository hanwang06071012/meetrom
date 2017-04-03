#-*- coding:utf-8 -*-
#============================================================
#作者：韩望
#日期：2017-04-02
#功能：默认函数更新：无
#备注：无
#============================================================
from flask import Flask,session,url_for
from flask import render_template,request
from pro import app
from pro.model.node_info  import NodeInfo
import json,sys
reload(sys)
sys.setdefaultencoding('utf-8')

@app.route('/',methods=['POST','GET'])
def show_default():
    current_id = 1
    tuple_slave_name =()
    if request.method=='POST':
        current_id = request.form['current_id',1]
    tuple_master_name = NodeInfo.select(cols='name',where=('node_id = %s'%(current_id)))
    if (current_id > 0 and current_id <= 3133):
        tuple_slave_name = NodeInfo.select(cols="name",where=('node_id > %s and node_id <= %s' % (current_id,current_id+3)))
    else:
        tuple_slave_name = NodeInfo.select(cols='name',where=('node_id = %s or node_id = %s or node_id = %s ' % (1,2,3)))
    print("=====================start ========================")
    print (tuple_name)
    session['master_city_name'] = tuple_master_name[0][0]
    session['frist_slave_name'] = tuple_slave_name[0][0]
    session['sed_slave_name'] = tuple_slave_name[1][0]
    session['thrid_slave_name'] = tuple_slave_name[2][0]
    print("=====================  end ========================")
    return render_template('default.html',**locals())

@app.route('/fangwuchuzu')
def fangwuchuzu():
	return render_template('sub1/fangwuchuzu.html')


@app.route('/selectaddr')
def selectaddr():
	return render_template('selectaddr.html')

@app.route('/test')
def test():
	return "hello world!"
