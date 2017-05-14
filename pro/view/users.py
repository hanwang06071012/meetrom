#-*- coding:utf-8 -*-
#============================================================
#作者：韩望
#日期：2017-04-02
#功能：默认视图函数
#默认函数更新：无
#备注：无
#============================================================
from flask import Flask,session,url_for
from flask import render_template,request,redirect
from pro import app
from pro.model.admin  import Admin
from pro.model.conference import Conference
from pro.model.storepicture import StorePicture
from pro.model.users import Users
import json,sys,time
from frame import const
reload(sys)
sys.setdefaultencoding('utf-8')

#用户列表
@app.route("/users/list")
def users_list():
    str_col = ("%s,%s,%s,%s,%s,%s" % ("ID","usersid","usersName","usersPhone","usersEmail","createDate"))
    tuple_result = Users.select(cols=str_col)
    return render_template("users_list.html",**locals())

#添加展示用户
@app.route("/users/add",methods=["POST","GET"])
def user_add():
    if request.method == 'POST':
        usersid =request.form["id"]
        usersName =request.form["user_name"]
        usersPass =request.form["passwd"]
        usersRepass=request.form["confirm_password"]
        usersTrueName =request.form["real_name"]
        usersAge =request.form["age"]
        usersSex=request.form["sex"]
        usersCsrq =request.form["date_birth"]
        usersHuji =request.form["household_registration"]
        usersJiguan=request.form["native_place"]
        usersIDcard=request.form["ID_number"]
        usersSpecialty=request.form["professional_title"]
        usersAddress =request.form["address"]
        usersEmail=request.form["user_mail"]
        usersPhone =request.form["contract_phone"]
        createDate=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        map_data = {"usersid":usersid,"usersName":usersName,"usersPass":usersPass,"usersRepass":usersRepass,"usersTrueName":usersTrueName,"usersAge":usersAge,"usersSex":usersSex,"usersCsrq":usersCsrq,"usersHuji":usersHuji,"usersJiguan":usersJiguan,"usersIDcard":usersIDcard,"usersSpecialty":usersSpecialty,"usersAddress":usersAddress,"usersEmail":usersEmail,"usersPhone":usersPhone,"createDate":createDate}
        Users.insert(map_data)
        return redirect(url_for("userlist"))
    else:
        pass
    return render_template("users_add.html")

#添加展示用户
@app.route("/users/select",methods=["POST","GET"])
def user_select():
    map_where ={}
    list_key_val = []
    str_sql_where=""
    if request.method == 'POST':
        usersid =request.form["id"]
        if len(usersid) != 0:
            map_where["usersid"] = usersid
        usersName =request.form["user_name"]
        if len(usersName) != 0:
            map_where["usersName"] = usersName
        usersTrueName =request.form["real_name"]
        if len(usersTrueName) != 0:
            map_where["usersTrueName"] = usersTrueName
        usersAge =request.form["age"]
        if len(usersAge) != 0:
            map_where["usersAge"] = usersAge
        usersSex=request.form["sex"]
        if len(usersSex) != 0:
            map_where["usersSex"] = usersSex
        usersHuji =request.form["household_registration"]
        if len(usersHuji) != 0:
            map_where["usersHuji"] = usersHuji
        usersJiguan=request.form["native_place"]
        if len(usersJiguan) != 0:
            map_where["usersJiguan"] = usersJiguan
        usersIDcard=request.form["ID_number"]
        if len(usersIDcard) != 0:
            map_where["usersIDcard"] = usersIDcard
        usersSpecialty=request.form["professional_title"]
        if len(usersSpecialty) != 0:
            map_where["usersSpecialty"] = usersSpecialty
        usersAddress =request.form["address"]
        if len(usersAddress) != 0:
            map_where["usersAddress"] = usersAddress
        usersEmail=request.form["user_mail"]
        if len(usersEmail) != 0:
            map_where["usersEmail"] = usersEmail
        usersPhone =request.form["contract_phone"]
        if len(usersPhone) != 0:
            map_where["usersPhone"] = usersPhone
        if len(map_where) != 0:
            for sig_map_where in map_where:
                    key = sig_map_where
                    val = map_where[key]
                    tuple_mid_key_val = (key,val)
                    list_key_val.append(tuple_mid_key_val)
        int_len_list_key_val = len(list_key_val)
        if int_len_list_key_val == 1:
            str_sql_mid = (" %s = '%s'" % (list_key_val[0][0],list_key_val[0][1]))
            str_sql_where += str_sql_mid
        elif int_len_list_key_val > 1:
            for i in range(int_len_list_key_val-1):
                str_sql_mid = (" %s = '%s' and " % (list_key_val[i][0],list_key_val[i][1]))
                str_sql_where += str_sql_mid
            str_sql_mid = (" %s = '%s' " % (list_key_val[int_len_list_key_val-1][0],list_key_val[int_len_list_key_val-1][1]))
            str_sql_where += str_sql_mid
        else:
            pass
        str_col = (" %s,%s,%s,%s,%s,%s " % ("ID","usersid","usersName","usersPhone","usersEmail","createDate"))
        tuple_result = Users.select(cols=str_col,where=str_sql_where)
        return render_template("users_list.html",**locals())
    else:
        pass
    return render_template("users_select.html")

#用户信息查询
@app.route("/user/<id>/info")
def userinfo(id):
    str_col = ("%s,%s,%s,%s,%s,%s" % ("ID","usersid","usersName","usersPhone","usersEmail","createDate"))
    tuple_result = Users.select(cols=str_col,where=("usersid=%s" % (id)))
    return render_template("users_list.html",**locals())
