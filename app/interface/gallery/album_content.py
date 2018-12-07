import json

import flask_login
from flask import Blueprint
from flask import request
from flask import Response

from app.application.album_content import AlbumContentQueryService
from app.application.category import CategoryQueryService
from app.application.folder import FolderQueryService
from app.application.file import FileQueryService
from lib.model.info.info import AuthorID
from lib.model.content import ContentID
from lib.model.album.album import AlbumID
from lib.model.user.user import User
from lib.model.category.category import CategoryID
from lib.model.info.info import AuthorID
from lib.model.category.category import CategoryID
from lib.model.info.info import AuthorID
from lib.model.folder.folder_factory import FolderFactory
from lib.model.info.info import AuthorID
from lib.model.folder.folder import FolderID
from lib.model.user.user import User
from lib.model.file.file import FileID

app_album_content_gallery = Blueprint('app_album_content_gallery', __name__)

# main で登録されているPATHからの相対パスで以下のURLを指定する
#  以下の場合のPATHは、/photo_log/album_content/file になる
#  - main.py のregister_blueprint が url_prefix='/photo_log/album_content'
#  - @app_album_content_gallery.route('/file')


# album_idに紐づくコンテンツ一覧を返す
@app_album_content_gallery.route('/', methods=['GET'])
#@flask_login.login_required
def album_content_index(album_id):
    album_id = AlbumID(album_id)
    if request.method == 'GET':
        album_content_query_service = AlbumContentQueryService()
        album_content_list = album_content_query_service.find_by_album_id(
            album_id)
        album_content_dict_list = album_content_list.to_dict()
        json_txt = json.dumps(album_content_dict_list, indent=4)
        return json_txt.encode("UTF-8")


# content_idに対する情報をかえす
@app_album_content_gallery.route('/<path:content_id>', methods=['GET'])
#@flask_login.login_required
def album_content(album_id, content_id):
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


# contentに紐づくフォルダーを返す
# content_がカテゴリーだった場合のみ
@app_album_content_gallery.route('/<path:content_id>/content', methods=['GET'])
def category_folder_index(album_id, content_id):
    album_id = AlbumID(album_id)
    content_id = CategoryID(content_id)
    if request.method == 'GET':
        album_content_query_service = AlbumContentQueryService()
        album_content = album_content_query_service.find_linked_content(
            album_id, content_id)
        if album_content is None:
            txt = 'content do not exist'
            return txt.encode("UTF-8")

        content_list_dict = album_content.to_dict()
        json_txt = json.dumps(content_list_dict, indent=4)
        return json_txt.encode("UTF-8")


# contentに紐づくフォルダーの情報を返す
# content_がカテゴリーだった場合のみ
@app_album_content_gallery.route(
    '/<path:content_id>/content/<path:folder_id>', methods=['GET'])
def folder(album_id, content_id, folder_id):
    album_id = AlbumID(album_id)
    content_id = CategoryID(content_id)
    folder_id = FolderID(folder_id)
    if request.method == 'GET':
        folder_query_service = FolderQueryService()
        folder_obj = folder_query_service.find(folder_id)
        if folder_obj is None:
            txt = 'folder do not exist'
            return txt.encode("UTF-8")

        folder_dict = folder_obj.to_dict()
        json_txt = json.dumps(folder_dict, indent=4)
        return json_txt.encode("UTF-8")


@app_album_content_gallery.route(
    '/<path:content_id>/content/<path:folder_id>/file', methods=['GET'])
def folder_file(album_id, content_id, folder_id):
    album_id = AlbumID(album_id)
    content_id = CategoryID(content_id)
    folder_id = FolderID(folder_id)
    if request.method == 'GET':
        folder_query_service = FolderQueryService()
        folder_obj = folder_query_service.find(folder_id)
        if folder_obj is None:
            txt = 'folder do not exist'
            return txt.encode("UTF-8")

        file_query_service = FileQueryService()
        file_list = file_query_service.find_by_folder(folder_obj)
        if file_list is None:
            txt = 'file do not exist'
            return txt.encode("UTF-8")

        file_list = file_list.to_dict()
        json_txt = json.dumps(file_list, indent=4)
        return json_txt.encode("UTF-8")


@app_album_content_gallery.route(
    '/<path:content_id>/content/<path:folder_id>/file/<path:file_id>',
    methods=['GET'])
def file_index(album_id, content_id, folder_id, file_id):
    if request.method == 'GET':
        file_query_service = FileQueryService()
        file = file_query_service.find(FileID(file_id))
        filename = '{}/{}'.format(file.location.path.value, file.name.value)
        f = open(filename, 'rb')
        image = f.read()
        return Response(response=image, content_type='image/jpeg')


@app_album_content_gallery.route(
    '/<path:content_id>/content/<path:folder_id>/file/thumb_small/<path:file_id>',
    methods=['GET'])
def file_index_thumb(album_id, content_id, folder_id, file_id):
    if request.method == 'GET':
        file_query_service = FileQueryService()
        file = file_query_service.find(FileID(file_id))
        filename = '{}/thumb_small/{}'.format(file.location.path.value,
                                              file.name.value)
        f = open(filename, 'rb')
        image = f.read()
        return Response(response=image, content_type='image/jpeg')
