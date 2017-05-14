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

#会议室列表
@app.route("/conference/list")
def conference_list():
    str_col = ("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % ("ID","Sqrzh","Sqrxm","Name","Didian","Duomeiti","Rongnarenshu","Hueiyizhuti","Shenqingzhuangtai","Shenpi","Shenqliyou","Shenqsjian"))
    tuple_result = Conference.select(cols=str_col)
    return render_template("conference_list.html",**locals())


#增加会议室
@app.route("/conference/add",methods=["POST","GET"])
def conference_add():
    if request.method == 'POST':
        Sqrzh =request.form["sqrzh"]
        Sqrxm =request.form["sqrxm"]
        Name =request.form["name"]
        Didian=request.form["didian"]
        Duomeiti =request.form["duomeiti"]
        Rongnarenshu =request.form["rongnarenshu"]
        Hueiyizhuti=request.form["hueiyizhuti"]
        Shenqingzhuangtai =request.form["shenqingzhuangtai"]
        Shenpi =request.form["shenpi"]
        Shenqliyou=request.form["shenqliyou"]
        Shenqsjian=request.form["shenqsjian"]
        map_data = {"Sqrzh":Sqrzh,"Sqrxm":Sqrxm,"Name":Name,"Didian":Didian,"Duomeiti":Duomeiti,"Rongnarenshu":Rongnarenshu,"Hueiyizhuti":Hueiyizhuti,"Shenqingzhuangtai":Shenqingzhuangtai,"Shenpi":Shenpi,"Shenqliyou":Shenqliyou,"Shenqsjian":Shenqsjian}
        Conference.insert(map_data)
        return redirect(url_for("conference_list"))
    else:
        pass
    return render_template("conference_add.html")

#展示会议室
@app.route("/conference/select",methods=["POST","GET"])
def conference_select():
    print("================conference select start=================================")
    map_where={}
    if request.method == 'POST':
        Sqrzh =request.form["sqrzh"]
        if len(Sqrzh) != 0:
            map_where["Sqrzh"] = Sqrzh
        Sqrxm =request.form["sqrxm"]
        if len(Sqrxm) != 0:
            map_where["Sqrxm"] = Sqrxm
        Name =request.form["name"]
        if len(Name) != 0:
            map_where["Name"] = Name
        Didian=request.form["didian"]
        if len(Didian) != 0:
            map_where["Didian"] = Didian
        Duomeiti =request.form["duomeiti"]
        if len(Duomeiti) != 0:
            map_where["Duomeiti"] = Duomeiti
        Rongnarenshu =request.form["rongnarenshu"]
        if len(Rongnarenshu) != 0:
            map_where["Rongnarenshu"] = Rongnarenshu
        Hueiyizhuti=request.form["hueiyizhuti"]
        if len(Hueiyizhuti) != 0:
            map_where["Hueiyizhuti"] = Hueiyizhuti
        Shenqingzhuangtai =request.form["shenqingzhuangtai"]
        if len(Shenqingzhuangtai) != 0:
            map_where["Shenqingzhuangtai"] = Shenqingzhuangtai
        Shenpi =request.form["shenpi"]
        if len(Shenpi) != 0:
            map_where["Shenpi"] = Shenpi
        Shenqliyou=request.form["shenqliyou"]
        if len(Shenqliyou) != 0:
            map_where["Shenqliyou"] = Shenqliyou
        Shenqsjian=request.form["shenqsjian"]
        if len(Shenqsjian) != 0:
            map_where["Shenqsjian"] = Shenqsjian
        print("================conference select come1=================================")
        print (map_where)
        if len(map_where) != 0:
            for sig_map_where in map_where:
                key = sig_map_where
                val = map_where[key]
                tuple_mid_key_val = (key,val)
                list_key_val.append(tuple_mid_key_val)
        int_len_list_key_val = len(list_key_val)
        print(list_key_val)
        print(int_len_list_key_val)
        if int_len_list_key_val == 1:
            str_sql_mid = (" %s = '%s'" % (list_key_val[0][0],list_key_val[0][1]))
            str_sql_where += str_sql_mid
        elif int_len_list_key_val > 1:
            for i in range(int_len_list_key_val-1):
                str_sql_mid = (" %s = '%s' and " % (list_key_val[i][0],list_key_val[i][1]))
                str_sql_where += str_sql_mid
                print (str_sql_mid)
                print(str_sql_where)
            str_sql_mid = (" %s = '%s' " % (list_key_val[int_len_list_key_val-1][0],list_key_val[int_len_list_key_val-1][1]))
            str_sql_where += str_sql_mid
            print (str_sql_mid)
            print(str_sql_where)
        else:
            pass
        str_col = ("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % ("ID","Sqrzh","Sqrxm","Name","Didian","Duomeiti","Rongnarenshu","Hueiyizhuti","Shenqingzhuangtai","Shenpi","Shenqliyou","Shenqsjian"))
        tuple_result = Conference.select(cols=str_col,where=str_sql_where)
        print(tuple_result)
        print("================conference select end1=================================")
        return render_template("conference_list.html",**locals())
    else:
        pass
    print("================conference select end2=================================")
    return render_template("conference_select.html")

#用户列表
@app.route("/conference/list")
def conferencelist():
    str_col = ("%s,%s,%s,%s,%s,%s" % ("ID","usersid","usersName","usersPhone","usersEmail","createDate"))
    tuple_result = Users.select(cols=str_col)
    return render_template("conference_list.html",**locals())
"""
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
    tuple_result = Users.select(cols=str_col,where=("usersid=%s" % (id)))
    return render_template("users_list.html",**locals())
"""