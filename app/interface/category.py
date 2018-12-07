# -*- coding: utf-8 -*-

import json

import flask_login
from flask import Blueprint
from flask import request

from lib.model.category.category import CategoryID
from app.application.category import CategoryQueryService
from app.application.category import CategoryCommandService
from app.application.folder import FolderQueryService
from lib.model.info.info import AuthorID
from lib.model.folder.folder import FolderID

app_category = Blueprint('app_category', __name__)

# main で登録されているPATHからの相対パスで以下のURLを指定する
#  以下の場合のPATHは、/photo_log/category/file になる
#  - main.py のregister_blueprint が url_prefix='/photo_log/category'
#  - @app_category.route('/file')


# カテゴリーに紐付けられたフォルダの一覧を取得できる /category/_id/folder/ - GET
@app_category.route('/<path:category_id>/folder', methods=['GET'])
@flask_login.login_required
def category_folder_index(category_id):
    user = flask_login.current_user
    author_id = AuthorID(user.user_id.value)
    if request.method == 'GET':
        category_id = CategoryID(category_id)
        category_query_service = CategoryQueryService()
        folder_list = category_query_service.find_linked_folder(category_id)
        if folder_list is None:
            txt = 'folder do not exist'
            return txt.encode("UTF-8")

        folder_list_dict = folder_list.to_dict()
        json_txt = json.dumps(folder_list_dict, indent=4)
        return json_txt.encode("UTF-8")


@app_category.route(
    '/<path:category_id>/folder/<path:folder_id>', methods=['POST', 'DELETE'])
@flask_login.login_required
def category(category_id, folder_id):
    user = flask_login.current_user
    author_id = AuthorID(user.user_id.value)
    category_id = CategoryID(category_id)
    folder_id = FolderID(folder_id)
    # カテゴリーにフォルダを紐付けることが出来る
    # /category/_id - POST {folder_id: folder-aaaaaaaaaaaaa}
    if request.method == 'POST':
        folder_query_service = FolderQueryService()
        folder = folder_query_service.find(folder_id)
        category_query_service = CategoryQueryService()
        category = category_query_service.find(category_id)
        category_command_service = CategoryCommandService()
        result = category_command_service.link_folder(category, folder)
        if result is False:
            txt = 'This folder can not link'
            return txt.encode("UTF-8")

        txt = 'create folder link'
        return txt.encode("UTF-8")

    # カテゴリーとフォルダの紐付けを外すことが出来る
    # /category/_id - DELETE {folder_id: folder-aaaaaaaaaaaaa}
    if request.method == 'DELETE':
        folder_query_service = FolderQueryService()
        folder = folder_query_service.find(folder_id)
        category_query_service = CategoryQueryService()
        category = category_query_service.find(category_id)
        category_command_service = CategoryCommandService()
        result = category_command_service.unlink_folder(category, folder)
        if result is False:
            txt = 'This folder can not unlink'
            return txt.encode("UTF-8")

        txt = 'delete folder link'
        return txt.encode("UTF-8")


@app_category.route('/<path:category_id>', methods=['GET'])
@flask_login.login_required
def category_get(category_id):
    user = flask_login.current_user
    if request.method == 'GET':
        category_id = CategoryID(category_id)
        category_query_service = CategoryQueryService()
        category = category_query_service.find(category_id)
        if category is None:
            txt = 'category do not exist'
            return txt.encode("UTF-8")

        category_dict = category.to_dict()
        json_txt = json.dumps(category_dict, indent=4)
        return json_txt.encode("UTF-8")
