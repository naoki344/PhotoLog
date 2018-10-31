# -*- coding: utf-8 -*-

import json

import flask_login
from flask import Blueprint
from flask import request

from app.application.album_category import AlbumCategoryCommandService
from app.application.album_category import AlbumCategoryQueryService
from lib.model.category.category import AuthorID
from lib.model.category.category import CategoryID
from lib.model.category.category import CategoryType
from lib.model.category.category_factory import CategoryFactory
from lib.model.user.user import User

app_album_category = Blueprint('app_album_category', __name__)

# main で登録されているPATHからの相対パスで以下のURLを指定する
#  以下の場合のPATHは、/photo_log/album_category/file になる
#  - main.py のregister_blueprint が url_prefix='/photo_log/album_category'
#  - @app_album_category.route('/file')


@app_album_category.route('/', methods=['GET', 'POST'])
# @flask_login.login_required
def album_category_index(user_id, album_id):

    album_category_author_id = user_id
    if request.method == 'GET':
        album_category_query_service = AlbumCategoryQueryService()
        user_album_category_list = album_category_query_service.find_user_all(
            AuthorID(album_category_author_id))
        album_category_dict_list = user_album_category_list.to_dict()
        json_txt = json.dumps(album_category_dict_list, indent=4)
        return json_txt.encode("UTF-8")

    if request.method == 'POST':
        post_data = request.json
        data = post_data.copy()
        data['category_type'] = CategoryType.ALBUM.name
        category_factory = CategoryFactory()
        album_category_obj = category_factory.create(data)
        if album_category_obj is False:
            txt = 'album_category can not create'
            return txt.encode("UTF-8")

        album_category_command_service = AlbumCategoryCommandService()
        registerd_album_category = album_category_command_service.register(
            album_category_obj)

        album_category_dict = registerd_album_category.to_dict()
        json_txt = json.dumps(album_category_dict, indent=4)
        return json_txt.encode("UTF-8")


@app_album_category.route(
    '/<path:album_category_id>', methods=['GET', 'PUT', 'DELETE'])
# @flask_login.login_required
def album_category(user_id, album_id, album_category_id):
    if request.method == 'GET':
        album_category_query_service = AlbumCategoryQueryService()
        album_category_obj = album_category_query_service.find(
            CategoryID(album_category_id))
        if album_category_obj is None:
            txt = 'album_category do not exist'
            return txt.encode("UTF-8")

        album_category_dict = album_category_obj.to_dict()
        json_txt = json.dumps(album_category_dict, indent=4)
        return json_txt.encode("UTF-8")

    if request.method == 'PUT':
        post_data = request.json

        album_category_query_service = AlbumCategoryQueryService()
        org_album_category = album_category_query_service.find(
            CategoryID(album_category_id))
        if org_album_category is None:
            txt = 'album_category do not exist'
            return txt.encode("UTF-8")

        new_album_category = org_album_category.modify(post_data)

        album_category_command_service = AlbumCategoryCommandService()
        updated_album_category = album_category_command_service.update(
            org_album_category, new_album_category)

        album_category_dict = updated_album_category.to_dict()
        json_txt = json.dumps(album_category_dict, indent=4)
        return json_txt.encode("UTF-8")

    if request.method == 'DELETE':
        post_data = request.json

        album_category_query_service = AlbumCategoryQueryService()
        org_album_category = album_category_query_service.find(
            CategoryID(album_category_id))

        album_category_command_service = AlbumCategoryCommandService()
        try:
            deleted_album_category = album_category_command_service.delete(
                org_album_category)
        except:
            msg = 'album_category[' + org_album_category.album_category_id.value + '] delete is failuer'
            return msg.encode("UTF-8")

        json_txt = json.dumps(deleted_album_category, indent=4)
        return json_txt.encode("UTF-8")
