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

#用户登陆界面
@app.route('/adminlogin',methods=["POST","GET"])
def showadminlogin():
    if request.method == "POST":
        user = request.form["user"]
        passwd = request.form["passwd"]
        usertype = request.form["usertype"]
        if usertype = 0:
            str_cols=(" %s,%s,%s" % ("ID","usersid","usersName"))
            str_where = (" (usersName='%s' and usersPass='%s') " % (user,passwd))
            tuple_id_name = Users.select(cols=str_cols,where=str_where)
        else:
            str_cols=(" %s,%s,%s" % ("ID","Adminid","AdminName"))
            str_where = (" (AdminName='%s' and AdminPass='%s') " % (user,passwd))
            tuple_id_name = Admin.select(cols=str_cols,where=str_where)
        if len(tuple_id_name) != 0:
            session["id"] = tuple_id_name[0][0]
            session["adminid"] = tuple_id_name[0][1]
            session["name"] = tuple_id_name[0][2]
            session["level"] = 0
            return render_template("admin.html",**locals())
        else:
            pass
    return render_template("admin_login.html")

@app.route('/userlogin',methods=["POST","GET"])
def user_login():
    if request.method == "POST":
        user = request.form["user"]
        passwd = request.form["passwd"]
        usertype = request.form["usertype"]
        if usertype = 1:
            str_cols=(" %s,%s,%s" % ("ID","usersid","usersName"))
            str_where = (" (usersName='%s' and usersPass='%s') " % (user,passwd))
            tuple_id_name = Users.select(cols=str_cols,where=str_where)
        else:

        if len(tuple_id_name) != 0:
            session["id"] = tuple_id_name[0][0]
            session["usersid"] = tuple_id_name[0][1]
            session["name"] = tuple_id_name[0][2]
            session["level"] = 1
            return render_template("admin.html",**locals())
        else:
            pass
    return render_template("user_login.html")

@app.route("/login/admin")
def adminlogin():
    return render_template("admin.html")

@app.route("/title/admin")
def admin_title():
    user="test"
    return render_template("admin_title.html",**locals())

@app.route("/sys/out")
def sys_out():
    session["id"] = ''
    session["adminid"] = ''
    session["name"] = ''
    session["level"] = -1
    return ("adminlogin")

