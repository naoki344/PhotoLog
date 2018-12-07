# -*- coding: utf-8 -*-

import json

import flask_login
from flask import Blueprint
from flask import request

from app.application.folder import FolderCommandService
from app.application.folder import FolderQueryService
from app.application.file import FileQueryService
from lib.model.folder.folder_factory import FolderFactory
from lib.model.info.info import AuthorID
from lib.model.folder.folder import FolderID
from lib.model.user.user import User

app_folder = Blueprint('app_folder', __name__)

# main で登録されているPATHからの相対パスで以下のURLを指定する
#  以下の場合のPATHは、/photo_log/folder/file になる
#  - main.py のregister_blueprint が url_prefix='/photo_log/folder'
#  - @app_folder.route('/file')


@app_folder.route('/', methods=['GET', 'POST'])
@flask_login.login_required
def folder_index():
    user = flask_login.current_user
    author_id = AuthorID(user.user_id.value)

    if request.method == 'GET':
        folder_query_service = FolderQueryService()
        user_folder_list = folder_query_service.find_user_all(author_id)
        folder_dict_list = user_folder_list.to_dict()
        json_txt = json.dumps(folder_dict_list, indent=4)
        return json_txt.encode("UTF-8")

    if request.method == 'POST':
        post_data = request.json
        data = post_data.copy()
        data['info']['author_id'] = user.user_id.value
        folder_factory = FolderFactory()
        folder_obj = folder_factory.create(data)
        if folder_obj is False:
            txt = 'folder can not create'
            return txt.encode("UTF-8")

        folder_command_service = FolderCommandService()
        registerd_folder = folder_command_service.register(folder_obj)

        folder_dict = registerd_folder.to_dict()
        json_txt = json.dumps(folder_dict, indent=4)
        return json_txt.encode("UTF-8")


@app_folder.route('/<path:folder_id>', methods=['GET', 'PUT', 'DELETE'])
@flask_login.login_required
def folder(folder_id):
    user = flask_login.current_user
    author_id = AuthorID(user.user_id.value)
    if request.method == 'GET':
        folder_query_service = FolderQueryService()
        folder_obj = folder_query_service.find(FolderID(folder_id))
        if folder_obj is None:
            txt = 'folder do not exist'
            return txt.encode("UTF-8")

        folder_dict = folder_obj.to_dict()
        json_txt = json.dumps(folder_dict, indent=4)
        return json_txt.encode("UTF-8")

    if request.method == 'PUT':
        post_data = request.json

        folder_query_service = FolderQueryService()
        org_folder = folder_query_service.find(FolderID(folder_id))
        if org_folder is None:
            txt = 'folder do not exist'
            return txt.encode("UTF-8")

        new_folder = org_folder.modify(post_data)

        folder_command_service = FolderCommandService()
        updated_folder = folder_command_service.update(org_folder, new_folder)

        folder_dict = updated_folder.to_dict()
        json_txt = json.dumps(folder_dict, indent=4)
        return json_txt.encode("UTF-8")

    if request.method == 'DELETE':
        post_data = request.json

        folder_query_service = FolderQueryService()
        org_folder = folder_query_service.find(FolderID(folder_id))

        folder_command_service = FolderCommandService()
        try:
            deleted_folder = folder_command_service.delete(org_folder)
        except:
            msg = 'folder[' + org_folder.folder_id.value + '] delete is failuer'
            return msg.encode("UTF-8")

        json_txt = json.dumps(deleted_folder, indent=4)
        return json_txt.encode("UTF-8")


@app_folder.route('/<path:folder_id>/file', methods=['GET'])
@flask_login.login_required
def folder_file(folder_id):
    user = flask_login.current_user
    author_id = AuthorID(user.user_id.value)
    if request.method == 'GET':
        folder_query_service = FolderQueryService()
        folder_obj = folder_query_service.find(FolderID(folder_id))
        if folder_obj is None:
            txt = 'folder do not exist'
            return txt.encode("UTF-8")

        file_query_service = FileQueryService()
        file_list = file_query_service.find_by_folder(folder_obj)

        file_list = file_list.to_dict()
        json_txt = json.dumps(file_list, indent=4)
        return json_txt.encode("UTF-8")
