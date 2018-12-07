# -*- coding: utf-8 -*-

import json

import flask_login
from flask import Blueprint
from flask import request
from flask import Response

from app.application.file import FileQueryService
from lib.model.file.file import FileID

app_file = Blueprint('app_file', __name__)

# main で登録されているPATHからの相対パスで以下のURLを指定する
#  以下の場合のPATHは、/photo_log/folder/file になる
#  - main.py のregister_blueprint が url_prefix='/photo_log/folder'
#  - @app_folder.route('/file')


@app_file.route('/<path:file_id>', methods=['GET'])
@flask_login.login_required
def file_index(file_id):
    user = flask_login.current_user
    author_id = AuthorID(user.user_id.value)
    if request.method == 'GET':
        file_query_service = FileQueryService()
        file = file_query_service.find(FileID(file_id))
        filename = '{}/{}'.format(file.location.path.value, file.name.value)
        f = open(filename, 'rb')
        image = f.read()
        return Response(response=image, content_type='image/jpeg')


@app_file.route('/thumb_small/<path:file_id>', methods=['GET'])
@flask_login.login_required
def file_index_thumb(file_id):
    user = flask_login.current_user
    author_id = AuthorID(user.user_id.value)
    if request.method == 'GET':
        file_query_service = FileQueryService()
        file = file_query_service.find(FileID(file_id))
        filename = '{}/thumb_small/{}'.format(file.location.path.value,
                                              file.name.value)
        f = open(filename, 'rb')
        image = f.read()
        return Response(response=image, content_type='image/jpeg')
