# -*- coding: utf-8 -*-
#
import sys
from flask import Flask
sys.path.append('/var/www/PhotoLog/api_interface/')
application = Flask(__name__)
@application.route('/photo_log')
def index():
    return 'HelloWorld'
