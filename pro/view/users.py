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
    print(request.method)
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
        print("id=%s,user_name=%s"%(id,user_name))
        map_data = {"usersid":str_id,"usersName":user_name,"usersPass":passwd,"usersRepass":confirm_password,"usersTrueName":real_name,"usersAge":age,"usersSex":sex,"usersCsrq":date_birth,"usersHuji":household_registration,"usersJiguan":native_place,"usersIDcard":ID_number,"usersSpecialty":professional_title,"usersAddress":address,"usersEmail":user_mail,"usersPhone":contract_phone}
        print("usersid=%s,userName=%s"%(str_id,user_name))
        print(map_data)
        Users.insert(map_data)
        return redirect(url_for("userlist"),**locals())
    else:
        pass
    return render_template("users_add.html")

