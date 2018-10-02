# -*- coding: utf-8 -*-

import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../')

from flask import Flask
from app.interface.folder import app_folder

application = Flask(__name__)
application.register_blueprint(app_folder,url_prefix='/photo_log/<string:user_id>/folder')

if __name__ == "__main__":
    application.run(debug=True)
