# -*- coding: utf-8 -*-

import json

import flask_login
from flask import Blueprint
from flask import request

from app.application.album_category import AlbumCategoryQueryService
from app.application.common_category import CommonCategoryQueryService
from app.application.folder import FolderQueryService
from app.application.album_content import AlbumContentCommandService
from app.application.album_content import AlbumContentQueryService
from lib.model.album_content.album_content_factory import AlbumContentFactory
from lib.model.info.info import AuthorID
from lib.model.content import Content
from lib.model.content import ContentID
from lib.model.album.album import AlbumID
from lib.model.user.user import User

app_album_content = Blueprint('app_album_content', __name__)

# main で登録されているPATHからの相対パスで以下のURLを指定する
#  以下の場合のPATHは、/photo_log/album_content/file になる
#  - main.py のregister_blueprint が url_prefix='/photo_log/album_content'
#  - @app_album_content.route('/file')


@app_album_content.route('/', methods=['GET', 'POST'])
@flask_login.login_required
def album_content_index(album_id):
    user = flask_login.current_user
    album_id = AlbumID(album_id)
    if request.method == 'GET':
        album_content_query_service = AlbumContentQueryService()
        album_content_list = album_content_query_service.find_by_album_id(
            album_id)
        album_content_dict_list = album_content_list.to_dict()
        json_txt = json.dumps(album_content_dict_list, indent=4)
        return json_txt.encode("UTF-8")

    if request.method == 'POST':
        post_data = request.json
        data = post_data.copy()
        data['info']['author_id'] = user.user_id.value
        content_id = ContentID(data['content_id'])
        content_command_service = _get_content_command_service(content_id)
        content = content_command_service.find(content_id)
        dict_data = {}
        dict_data['album_id'] = album_id
        dict_data['content'] = content
        album_content_factory = AlbumContentFactory()
        album_content = album_content_factory.create(dict_data)
        if album_content is False:
            txt = 'album_content can not create'
            return txt.encode("UTF-8")

        album_content_command_service = AlbumContentCommandService()
        album_content_command_service.register(album_content)

        album_content_dict = album_content.to_dict()
        json_txt = json.dumps(album_content_dict, indent=4)
        return json_txt.encode("UTF-8")


@app_album_content.route('/<path:content_id>', methods=['GET', 'DELETE'])
@flask_login.login_required
def album_content(album_id, content_id):
    user = flask_login.current_user
    content_id = ContentID(content_id)
    album_id = AlbumID(album_id)
    if request.method == 'GET':
        album_content_query_service = AlbumContentQueryService()
        album_content = album_content_query_service.find(album_id, content_id)
        if album_content is None:
            txt = 'album_content do not exist'
            return txt.encode("UTF-8")

        album_content_dict = album_content.to_dict()
        json_txt = json.dumps(album_content_dict, indent=4)
        return json_txt.encode("UTF-8")

    if request.method == 'DELETE':
        post_data = request.json

        try:
            album_content_query_service = AlbumContentQueryService()
            org_album_content = album_content_query_service.find(
                album_id, content_id)
            album_content_command_service = AlbumContentCommandService()
            album_content_command_service.delete(org_album_content)
        except:
            msg = 'album_content[' + org_album_content.album_id.value + '] delete is failuer'
            return msg.encode("UTF-8")

        json_txt = json.dumps(org_album_content.to_dict(), indent=4)
        return json_txt.encode("UTF-8")


def _get_content_command_service(content_id: ContentID):
    content_type = Content.check_content_type(content_id)
    if content_type == 'folder':
        return FolderQueryService()
    if content_type == 'common_category':
        return CommonCategoryQueryService()
    if content_type == 'album_category':
        return AlbumCategoryQueryService()
