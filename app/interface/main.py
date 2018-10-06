# -*- coding: utf-8 -*-

import os
import random
import string
import sys

import flask_login
from flask import Flask
from flask import redirect
from flask import request
from flask import url_for

from app.application.user import UserFindService
from app.interface.folder import app_folder
from lib.model.user.user import User
from lib.model.user.user import UserID

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../')

application = Flask(__name__)
application.register_blueprint(
    app_folder, url_prefix='/photo_log/<string:user_id>/folder')
application.secret_key = "".join([
    random.choice(string.ascii_letters + string.digits + '_' + '-' + '!' +
                  '#' + '&') for i in range(64)
])

#############################################################
# user_loginがBlueprintに対応していないため、mainに記入する #
#############################################################
login_manager = flask_login.LoginManager()
login_manager.init_app(application)


@login_manager.user_loader
def load_user(user_id):
    user = UserFindService().find(UserID(user_id))
    if user is None:
        return
    return user


@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized'


@login_manager.request_loader
def request_loader(request):
    user_id = request.form.get('user_id')
    user = UserFindService().find(UserID(user_id))
    if user is None:
        return

    if user.auth(request.form['password']):
        return user


@application.route('/photo_log/user/login', methods=['GET', 'POST'])
def login():
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


if __name__ == "__main__":
    application.run(debug=True)
