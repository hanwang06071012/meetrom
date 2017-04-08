#-*- coding:utf-8 -*-
#============================================================
#作者：韩望
#日期：2017-04-02
#功能：默认视图函数
#默认函数更新：无
#备注：无
#============================================================
from flask import Flask,session,url_for
from flask import render_template,request
from pro import app
from pro.model.node_info  import NodeInfo
from pro.model.income import Income
from pro.model.estate_agents import EstateAgents
import json,sys
from frame import const
reload(sys)
sys.setdefaultencoding('utf-8')

def init_addr(current_id):
    #current_id = const.DEFAULTCITYID
    tuple_slave_name =()
    #if request.method=='GET':
        #current_id = request.values.get('current_id',default=const.DEFAULTCITYID)
    current_id = int(current_id)
    if (current_id > const.INITCITYNODEID and current_id <= (const.MAXCITYNODEID - const.CITYNODEIDOFFSET)):
        tuple_slave_name = NodeInfo.select(cols="name",where=('node_id > %s and node_id <= %s' % (current_id,current_id+const.CITYNODEIDOFFSET)))
        session['master_city_id'] = current_id
        session['frist_slave_city_id'] = current_id + const.CITYNODEIDOFFSETONE
        session['sed_slave_city_id'] = current_id + const.CITYNODEIDOFFSESED
        session['thrid_slave_city_id'] = current_id + const.CITYNODEIDOFFSET
    elif (current_id < const.INITCITYNODEID or current_id > const.MAXCITYNODEID):
        current_id = const.DEFAULTCITYID
        session['master_city_id'] = current_id
        session['frist_slave_city_id'] = const.CITYNODEIDSED
        session['sed_slave_city_id'] = const.CITYNODEIDTHREE
        session['thrid_slave_city_id'] = const.CITYNODEIDFOURTH
        tuple_slave_name = NodeInfo.select(cols='name',where=('node_id = %s or node_id = %s or node_id = %s ' % (const.CITYNODEIDSED,const.CITYNODEIDTHREE,const.CITYNODEIDFOURTH)))
    else:
        session['master_city_id'] = current_id
        session['frist_slave_city_id'] = const.CITYNODEIDONE
        session['sed_slave_city_id'] = const.CITYNODEIDSED
        session['thrid_slave_city_id'] = const.CITYNODEIDTHREE
        tuple_slave_name = NodeInfo.select(cols='name',where=('node_id = %s or node_id = %s or node_id = %s ' % (const.CITYNODEIDONE,const.CITYNODEIDSED,const.CITYNODEIDTHREE)))
    tuple_master_name = NodeInfo.select(cols='name',where=('node_id = %s'%(session['master_city_id'])))
    session['master_city_name'] = tuple_master_name[0][const.CITYLOCATIONINARRAY]
    session['frist_slave_city_name'] = tuple_slave_name[0][const.CITYLOCATIONINARRAY]
    session['sed_slave_city_name'] = tuple_slave_name[1][const.CITYLOCATIONINARRAY]
    session['thrid_slave_city_name'] = tuple_slave_name[2][const.CITYLOCATIONINARRAY]

#检查地址是否存在，不存在就初始化
def check_addr():
    try:
        current_id = session['master_city_id']
        if (len(session['master_city_name'])==0):
            if (current_id==''):
                init_addr(const.DEFAULTCITYID)
            else:
                init_addr(current_id)
        else:
            if (current_id !=''):
                init_addr(current_id)
            else:
                pass
    except:
        init_addr(const.DEFAULTCITYID)
    return ""

#地址设置
@app.route("/set/addr",methods=['POST'])
def set_addr():
    try:
        current_city_id = request.values.get("str_node_id",default="")
        if (len(current_city_id) != 0):
            init_addr(current_city_id)
            return ""
        else:
            return "set city failure...."    
    except:
        return "set city failure...."

@app.route('/',methods=['POST','GET'])
def show_default():
    check_addr()
    return render_template('default.html',**locals())

@app.route('/fangwuchuzu',methods=['POST','GET'])
def fangwuchuzu():
    check_addr()
    return render_template('sub1/fangwuchuzu.html',**locals())

@app.route('/fangwuchaxun',methods=['POST','GET'])
def fangwuchaxun():
    check_addr()
    list_city_names = []
    list_ciyt_fangzu=[]
    list_agent_names=[]
    map_fangchan_chaxun = {}

    current_city_id = session['master_city_id']
    tuple_city_names=NodeInfo.select(cols='name',where=("parent_id=%s" % current_city_id))
    try:
        for sig_city_names in tuple_city_names:
            sig_city_name = sig_city_names[0]
            list_city_names.append(sig_city_name)
    except:
        pass
    map_fangchan_chaxun["city_names"] = list_city_names

    tuple_city_category=NodeInfo.select(cols='category',where=("node_id=%s" % current_city_id))
    current_category = tuple_city_category[0][0]
    tuple_city_incomes = Income.select(cols="frist_level,second_level,thrid_level,forth_level,fifth_level,sixth_level,seventh_level,eigth_level",where=("city_type=%s" % current_category))
    try:
        for sig_city_incomes in tuple_city_incomes:
            for sig_city_income in sig_city_incomes:
                list_ciyt_fangzu.append(sig_city_income/4)
    except:
        pass
    map_fangchan_chaxun["fang_zu"] = list_ciyt_fangzu

    tuple_agent_names = EstateAgents.select(cols="name",where=("level <= %s" % current_category))
    try:
        for sig_agent_names in tuple_agent_names:
            for sig_agent_name in sig_agent_names:
                list_agent_names.append[sig_agent_name]
    except:
        pass
    map_fangchan_chaxun['agents_names'] = list_agent_names

    json_fangchan_chaxun_result = json.dumps(map_fangchan_chaxun)
    return (json_fangchan_chaxun_result)

@app.route('/selectaddr')
def selectaddr():
	return render_template('selectaddr.html')

@app.route('/test')
def test():
	return "hello world!"
