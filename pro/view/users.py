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
import json,sys
from frame import const
reload(sys)
sys.setdefaultencoding('utf-8')

#用户列表
@app.route("/users/list")
def userlist():
    str_col = ("%s,%s,%s,%s,%s,%s" % ("ID","usersid","usersName","usersPhone","usersEmail","createDate"))
    tuple_result = Users.select(cols=str_col)
    return render_template("users_list.html",**locals())

#添加展示用户
@app.route("/users/add",methods=["POST","GET"])
def user_add():
    if request.method == 'POST':
        str_id =request.form["id"]
        user_name =request.form["user_name"]
        passwd =request.form["passwd"]
        confirm_password=request.form["confirm_password"]
        real_name =request.form["real_name"]
        age =request.form["age"]
        sex=request.form["sex"]
        date_birth =request.form["date_birth"]
        household_registration =request.form["household_registration"]
        native_place=request.form["native_place"]
        ID_number=request.form["ID_number"]
        professional_title=request.form["professional_title"]
        address =request.form["address"]
        user_mail=request.form["user_mail"]
        contract_phone =request.form["contract_phone"]
        map_data = {"usersid":str_id,"usersName":user_name,"usersPass":passwd,"usersRepass":confirm_password,"usersTrueName":real_name,"usersAge":age,"usersSex":sex,"usersCsrq":date_birth,"usersHuji":household_registration,"usersJiguan":native_place,"usersIDcard":ID_number,"usersSpecialty":professional_title,"usersAddress":address,"usersEmail":user_mail,"usersPhone":contract_phone}
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
        str_id =request.form["id"]
        if len(str_id) != 0:
            map_where["usersid"] = str_id
        user_name =request.form["user_name"]
        if len(user_name) != 0:
            map_where["usersName"] = user_name
        real_name =request.form["real_name"]
        if len(real_name) != 0:
            map_where["usersTrueName"] = real_name
        age =request.form["age"]
        if len(age) != 0:
            map_where["usersAge"] = age
        sex=request.form["sex"]
        if len(sex) != 0:
            map_where["usersSex"] = sex
        household_registration =request.form["household_registration"]
        if len(household_registration) != 0:
            map_where["usersHuji"] = household_registration
        native_place=request.form["native_place"]
        if len(native_place) != 0:
            map_where["usersJiguan"] = native_place
        ID_number=request.form["ID_number"]
        if len(ID_number) != 0:
            map_where["usersIDcard"] = ID_number
        professional_title=request.form["professional_title"]
        if len(professional_title) != 0:
            map_where["usersSpecialty"] = professional_title
        address =request.form["address"]
        if len(address) != 0:
            map_where["usersAddress"] = address
        user_mail=request.form["user_mail"]
        if len(user_mail) != 0:
            map_where["usersEmail"] = user_mail
        contract_phone =request.form["contract_phone"]
        if len(contract_phone) != 0:
            map_where["usersPhone"] = contract_phone
        if len(map_where) != 0:
            for sig_map_where in map_where:
                for key,val in sig_map_where:
                    tuple_mid_key_val = (key,val)
                    list_key_val.append(tuple_mid_key_val)
        int_len_list_key_val = len(list_key_val)
        if int_len_list_key_val == 1:
            str_sql_mid = (" %s like '%%%s%%'" % (list_key_val[0][0],list_key_val[0][1]))
            str_sql_where += str_sql_mid
        elif int_len_list_key_val > 1:
            for i in range(int_len_list_key_val-1):
                str_sql_mid = (" %s like %%%s%% and " % (list_key_val[i][0],list_key_val[i][1]))
                str_sql_where += str_sql_mid
            str_sql_mid += (" %s like %%%s%%" % (list_key_val[int_len_list_key_val-1][0],list_key_val[int_len_list_key_val-1][1]))
            str_sql_where += str_sql_mid
        else:
            pass
        str_col = ("%s,%s,%s,%s,%s,%s" % ("ID","usersid","usersName","usersPhone","usersEmail","createDate"))
        tuple_result = Users.select(cols=str_col,where=str_sql_where)
        return render_template("users_list.html",**locals())
    else:
        pass
    return render_template("users_select.html")

#用户信息查询
@app.route("/user/<id>/info")
def userinfo(id):
    str_col = ("%s,%s,%s,%s,%s,%s" % ("ID","usersid","usersName","usersPhone","usersEmail","createDate"))
    tuple_result = Users.select(cols=str_col,where=("id=%s" % (id)))
    return render_template("users_list.html",**locals())
