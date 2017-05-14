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

#用户信息查询
@app.route("/admin/list")
def admin_list():
    try:
        str_col = ("%s,%s,%s,%s,%s,%s" % ("ID","Adminid","AdminName","AdminPhone","AdminEmail","AdminCsrq"))
        tuple_result = Admin.select(cols=str_col)
        return render_template("admin_list.html",**locals())
    except:
        return redirect(url_for("userlist"))


#用户信息查询
@app.route("/admin/<id>/info")
def admin_info(id):
    try:
        str_col = ("%s,%s,%s,%s,%s,%s" % ("ID","Adminid","AdminName","AdminPhone","AdminEmail","AdminCsrq"))
        tuple_result = Admin.select(cols=str_col,where=("usersid=%s" % (id)))
        return render_template("admin_list.html",**locals())
    except:
        return redirect(url_for("userlist"))

#管理员修改个人资料
@app.route("/admin/<id>/edit",methods=["POST","GET"])
def admin_info_edit(id):
    map_where={}
    if request.method == "POST":
        Adminid =request.form["adminid"]
        if len(Adminid) != 0:
            map_where["Adminid"] = Adminid
        AdminName =request.form["adminName"]
        if len(AdminName) != 0:
            map_where["AdminName"] = AdminName
        AdminTrueName =request.form["adminTrueName"]
        if len(AdminTrueName) != 0:
            map_where["AdminTrueName"] = AdminTrueName
        AdminAddress =request.form["adminAddress"]
        if len(AdminAddress) != 0:
            map_where["AdminAddress"] = AdminAddress
        AdminEmail =request.form["adminEmail"]
        if len(AdminEmail) != 0:
            map_where["AdminEmail"] = AdminEmail
        AdminSpecialty =request.form["adminSpecialty"]
        if len(AdminSpecialty) != 0:
            map_where["AdminSpecialty"] = AdminSpecialty
        AdminHuji =request.form["adminHuji"]
        if len(AdminHuji) != 0:
            map_where["AdminHuji"] = AdminHuji
        AdminIDcard =request.form["adminIDcard"]
        if len(AdminIDcard) != 0:
            map_where["AdminIDcard"] = AdminIDcard
        AdminCsrq =request.form["adminCsrq"]
        if len(AdminCsrq) != 0:
            map_where["AdminCsrq"] = AdminCsrq
        AdminJiguan =request.form["adminJiguan"]
        if len(AdminJiguan) != 0:
            map_where["AdminJiguan"] = AdminJiguan
        AdminAge =request.form["adminAge"]
        if len(AdminAge) != 0:
            map_where["AdminAge"] = AdminAge
        AdminSex =request.form["adminSex"]
        if len(AdminSex) != 0:
            map_where["AdminSex"] = AdminSex
        AdminPhone =request.form["adminPhone"]
        if len(AdminPhone) != 0:
            map_where["AdminPhone"] = AdminPhone
        str_sql_where = (" ID = %s" % id)
        Admin.update_dict(data=map_where,where=str_sql_where)
        return redirect(url_for("admin_list"))
    str_col = ("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % ("Adminid","AdminName","AdminTrueName","AdminAddress","AdminEmail","AdminSpecialty","AdminHuji","AdminIDcard","AdminCsrq","AdminJiguan","AdminAge","AdminSex","AdminPhone"))
    tuple_result = Admin.select(cols=str_col,where=(" ID = %s" % (id)))
    return render_template("admin_edit.html",**locals())