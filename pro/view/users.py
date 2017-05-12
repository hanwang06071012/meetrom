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

@app.route("/users/list")
def userlist():
    str_col = ("%s,%s,%s,%s,%s,%s" % ("ID","usersid","usersName","usersEmail","createDate","usersPhone"))
    tuple_result = Users.select(cols=str_col)
    print("============================start============================")
    print (tuple_result)
    pirnt("============================end============================")
    return render_template("users_list.html",**locals())
