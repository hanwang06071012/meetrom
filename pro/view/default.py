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
        if usertype == "0":
            str_cols=(" %s,%s,%s" % ("ID","usersid","usersName"))
            str_where = (" (usersName='%s' and usersPass='%s') " % (user,passwd))
            tuple_id_name = Users.select(cols=str_cols,where=str_where)
            session["level"] = 1
        else:
            str_cols=(" %s,%s,%s" % ("ID","Adminid","AdminName"))
            str_where = (" (AdminName='%s' and AdminPass='%s') " % (user,passwd))
            tuple_id_name = Admin.select(cols=str_cols,where=str_where)
            session["level"] = 0
        if len(tuple_id_name) != 0:
            session["id"] = tuple_id_name[0][0]
            session["adminid"] = tuple_id_name[0][1]
            session["name"] = tuple_id_name[0][2]
            return render_template("admin.html",**locals())
        else:
            pass
    return render_template("admin_login.html")

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
@app.route("/info/<id>/<level>/delete")
def info_delete(id,level):
    str_sql_where = (" ID = %s ")
    if level=='0':
        Admin.delete(str_sql_where,[id])
    else:
        Users.delete(str_sql_where,[id])

