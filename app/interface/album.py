# -*- coding: utf-8 -*-

import json

import flask_login
from flask import Blueprint
from flask import request

from app.application.album import AlbumCommandService
from app.application.album import AlbumQueryService
from lib.model.album.album import AuthorID
from lib.model.album.album import AlbumID
from lib.model.album.album_factory import AlbumFactory
from lib.model.user.user import User

app_album = Blueprint('app_album', __name__)

# main で登録されているPATHからの相対パスで以下のURLを指定する
#  以下の場合のPATHは、/photo_log/album/file になる
#  - main.py のregister_blueprint が url_prefix='/photo_log/album'
#  - @app_album.route('/file')


@app_album.route('/', methods=['GET', 'POST'])
# @flask_login.login_required
def album_index(user_id):

    album_author_id = user_id
    if request.method == 'GET':
        album_query_service = AlbumQueryService()
        user_album_list = album_query_service.find_user_all(
            AuthorID(album_author_id))
        album_dict_list = user_album_list.to_dict()
        json_txt = json.dumps(album_dict_list, indent=4)
        return json_txt.encode("UTF-8")

    if request.method == 'POST':
        post_data = request.json
        data = post_data.copy()
        album_factory = AlbumFactory()
        album_obj = album_factory.create(data)
        if album_obj is False:
            txt = 'album can not create'
            return txt.encode("UTF-8")

        album_command_service = AlbumCommandService()
        registerd_album = album_command_service.register(album_obj)

        album_dict = registerd_album.to_dict()
        json_txt = json.dumps(album_dict, indent=4)
        return json_txt.encode("UTF-8")


@app_album.route('/<path:album_id>', methods=['GET', 'PUT', 'DELETE'])
# @flask_login.login_required
def album(user_id, album_id):
    album_author_id = user_id
    if request.method == 'GET':
        album_query_service = AlbumQueryService()
        album_obj = album_query_service.find(AlbumID(album_id))
        if album_obj is None:
            txt = 'album do not exist'
            return txt.encode("UTF-8")

        album_dict = album_obj.to_dict()
        json_txt = json.dumps(album_dict, indent=4)
        return json_txt.encode("UTF-8")

    if request.method == 'PUT':
        post_data = request.json

        album_query_service = AlbumQueryService()
        org_album = album_query_service.find(AlbumID(album_id))
        if org_album is None:
            txt = 'album do not exist'
            return txt.encode("UTF-8")

        new_album = org_album.modify(post_data)

        album_command_service = AlbumCommandService()
        updated_album = album_command_service.update(org_album, new_album)

        album_dict = updated_album.to_dict()
        json_txt = json.dumps(album_dict, indent=4)
        return json_txt.encode("UTF-8")

    if request.method == 'DELETE':
        post_data = request.json

        album_query_service = AlbumQueryService()
        org_album = album_query_service.find(AlbumID(album_id))

        album_command_service = AlbumCommandService()
        try:
            deleted_album = album_command_service.delete(org_album)
        except:
            msg = 'album[' + org_album.album_id.value + '] delete is failuer'
            return msg.encode("UTF-8")

        json_txt = json.dumps(deleted_album, indent=4)
        return json_txt.encode("UTF-8")
