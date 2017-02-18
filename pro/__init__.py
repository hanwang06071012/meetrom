#-*- coding:utf-8 -*-
from flask import Flask

#-----------create app----------
app = Flask(__name__)
app.config.from_object("pro.config")

from view import default
