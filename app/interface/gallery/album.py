import json

import flask_login
from flask import Blueprint
from flask import request

from app.application.album import AlbumQueryService
from lib.model.info.info import AuthorID
from lib.model.album.album import AlbumID
from lib.model.album.album_factory import AlbumFactory
from lib.model.user.user import User

app_album_gallery = Blueprint('app_album_gallery', __name__)

# main で登録されているPATHからの相対パスで以下のURLを指定する
#  以下の場合のPATHは、/photo_log/album/file になる
#  - main.py のregister_blueprint が url_prefix='/photo_log/album'
#  - @app_album_gallery.route('/file')


@app_album_gallery.route('/', methods=['GET', 'POST'])
@flask_login.login_required
def album_gallery_index():
    user = flask_login.current_user
    if request.method == 'GET':
        author_id = AuthorID(user.user_id.value)
        album_query_service = AlbumQueryService()
        user_album_list = album_query_service.find_user_all(author_id)
        album_dict_list = user_album_list.to_dict()
        json_txt = json.dumps(album_dict_list, indent=4)
        return json_txt.encode("UTF-8")


@app_album_gallery.route('/<path:album_id>', methods=['GET', 'PUT', 'DELETE'])
@flask_login.login_required
def album(album_id):
    user = flask_login.current_user
    if request.method == 'GET':
        album_query_service = AlbumQueryService()
        album_obj = album_query_service.find(AlbumID(album_id))
        if album_obj is None:
            txt = 'album do not exist'
            return txt.encode("UTF-8")

        album_dict = album_obj.to_dict()
        json_txt = json.dumps(album_dict, indent=4)
        return json_txt.encode("UTF-8")
