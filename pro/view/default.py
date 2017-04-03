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
from frame import const
reload(sys)
sys.setdefaultencoding('utf-8')

@app.route('/',methods=['POST','GET'])
def show_default():
    current_id = const.DEFAULTCITYID
    tuple_slave_name =()
    if request.method=='GET':
        current_id = request.values.get('current_id',default=1)
        current_id = int(current_id)
    if (current_id > 0 and current_id <= (const.MAXCITYNODE - const.CITYOFFSET)):
        tuple_slave_name = NodeInfo.select(cols="name",where=('node_id > %s and node_id <= %s' % (current_id,current_id+3)))
        session['master_city_id'] = current_id
        session['frist_slave_city_id'] = current_id + 1
        session['sed_slave_city_id'] = current_id +2
        session['thrid_slave_city_id'] = current_id +3
    elif (current_id < 0 or current_id > const.MAXCITYNODE):
        current_id = 1
        session['master_city_id'] = current_id
        session['frist_slave_city_id'] = 2
        session['sed_slave_city_id'] = 3
        session['thrid_slave_city_id'] = 4
        tuple_slave_name = NodeInfo.select(cols='name',where=('node_id = %s or node_id = %s or node_id = %s ' % (2,3,4)))
    else:
        session['master_city_id'] = current_id
        session['frist_slave_city_id'] = 1
        session['sed_slave_city_id'] = 2
        session['thrid_slave_city_id'] = 3
        tuple_slave_name = NodeInfo.select(cols='name',where=('node_id = %s or node_id = %s or node_id = %s ' % (1,2,3)))
    tuple_master_name = NodeInfo.select(cols='name',where=('node_id = %s'%(current_id)))
    session['master_city_name'] = tuple_master_name[0][0]
    session['frist_slave_city_name'] = tuple_slave_name[0][0]
    session['sed_slave_city_name'] = tuple_slave_name[1][0]
    session['thrid_slave_city_name'] = tuple_slave_name[2][0]
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
