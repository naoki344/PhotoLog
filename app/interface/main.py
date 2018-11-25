# -*- coding: utf-8 -*-

import json
import os
import random
import string
import sys

import flask_login
from flask_cors import CORS
from flask import Flask
from flask import redirect
from flask import request
from flask import url_for
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../')

from app.application.user import UserFindService
from app.application.user import UserRegisterService
from app.interface.folder import app_folder
from app.interface.album import app_album
from app.interface.common_category import app_common_category
from app.interface.album_category import app_album_category
from app.interface.album_content import app_album_content
from app.interface.category import app_category
from app.interface.file import app_file
from lib.model.user.user import User
from lib.model.user.user import UserID
from lib.model.user.user_factory import UserFactory

application = Flask(__name__)
CORS(application, supports_credentials=True)

application.secret_key = "".join([
    random.choice(string.ascii_letters + string.digits + '_' + '-' + '!' +
                  '#' + '&') for i in range(64)
])

application.register_blueprint(
    app_folder, url_prefix='/<string:user_id>/folder')

application.register_blueprint(app_album, url_prefix='/<string:user_id>/album')

application.register_blueprint(
    app_album_category,
    url_prefix='/<string:user_id>/album/<string:album_id>/album_category/')

application.register_blueprint(
    app_album_content,
    url_prefix='/<string:user_id>/album/<string:album_id>/album_content/')

application.register_blueprint(
    app_common_category, url_prefix='/<string:user_id>/common_category')

application.register_blueprint(
    app_category, url_prefix='/<string:user_id>/category')

application.register_blueprint(app_file, url_prefix='/<string:user_id>/file')

#############################################################
# user_loginがBlueprintに対応していないため、mainに記入する #
#############################################################
login_manager = flask_login.LoginManager()
login_manager.init_app(application)


@application.route('/user/login', methods=['GET', 'POST'])
def user_login():
    if request.method == 'GET':
        return '''
               <form action='login' method='POST'>
                <input type='text' name='user_id' id='user_id' placeholder='email'/>
                <input type='password' name='password' id='password' placeholder='password'/>
                <input type='submit' name='submit'/>
               </form>
               '''

    user_id = request.form.get('user_id')
    user = UserFindService().find(UserID(user_id))
    if user is None:
        return 'User Not Found'

    if user.auth(request.form['password']):
        flask_login.login_user(user)
        return redirect(url_for('app_folder.folder_index', user_id=user_id))

    return 'Bad login'


@application.route('/photo_log/user/register', methods=['GET', 'POST'])
def user_register():
    request_dict = request.json

    user_obj = UserFactory().create(request_dict)
    txt = user_obj
    if user_obj is False:
        txt = 'User can not register'
        return txt.encode("UTF-8")

    registerd_user = UserRegisterService().register(user_obj)

    #user_dict = registerd_user.to_dict()
    #json_txt = json.dumps(user_dict, indent=4)
    json_txt = 'OK'
    return json_txt.encode("UTF-8")


@login_manager.user_loader
def load_user(user_id):
    user = UserFindService().find(UserID(user_id))
    if user is None:
        return
    return user


@login_manager.unauthorized_handler
def unauthorized_handler():
    return redirect(url_for('user_login'))


@login_manager.request_loader
def request_loader(request):
    user_id = request.form.get('user_id')
    user = UserFindService().find(UserID(user_id))
    if user is None:
        return

    if user.auth(request.form['password']):
        return user


if __name__ == "__main__":
    application.run(debug=True)
