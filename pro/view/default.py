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

@app.route('/adminlogin',methods=["POST","GET"])
def showadminlogin():
    print("come to 1")
    if request.method == "POST":
        print("come to 2")
        user = request.form["user"]
        passwd = request.form["passwd"]
        str_cols=(" %s,%s" % ("Adminid","AdminName"))
        print("come to 3")
        str_where = (" (AdminName='%s' and AdminPass='%s') " % (user,passwd))
        print(str_where)
        tuple_id_name = Admin.select(cols=str_cols,where=str_where)
        if len(tuple_id_name) != 0:
            session["id"] = tuple_id_name[0][0]
            session["name"] = tuple_id_name[0][1]
            session["level"] = 0
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

