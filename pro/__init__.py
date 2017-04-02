#-*- coding:utf-8 -*-
from flask import Flask

#-----------create app----------
app = Flask(__name__)
app.config.from_object("frame.config")
app.config['SECRET_KEY'] = '123456'

from view import default
