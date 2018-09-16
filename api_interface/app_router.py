# -*- coding: utf-8 -*-

import sys,os
from flask import Flask
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')
from app.interface.folder import GetUserAllFolder

application = Flask(__name__)
@application.route('/photo_log')
def index():
    data = GetUserAllFolder(1)
    json = data.get_json()
    return json.encode("UTF-8")
