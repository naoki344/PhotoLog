# -*- coding: utf-8 -*-

import json
from app.application.folder import FolderQueryService
from app.application.folder import FolderCommandService
from lib.model.folder.folder import FolderAuthorID
from flask import Blueprint
from flask import request


app_folder = Blueprint('app_folder',__name__)


#main で登録されているPATHからの相対パスで以下のURLを指定する
#  以下の場合のPATHは、/photo_log/folder/file になる
#  - main.py のregister_blueprint が url_prefix='/photo_log/folder'
#  - @app_folder.route('/file')

@app_folder.route( '/', methods=['POST','GET','PUT','DELETE'] )
def folder_index():
    if request.method == 'GET':
        folder_author_id = 1
        folder_service = FolderQueryService()
        json_txt = folder_service.find_all_folder(folder_author_id)
        return json_txt.encode("UTF-8")

    if request.method == 'POST':
        post_data = request.form
        json_txt = json.dumps( post_data ,indent=4)
        folder_service = FolderCommandService()
        data = [
            post_data["author_id"],
            post_data["name"],
            post_data["description"],
            post_data["release_status"],
            post_data["share_range"],
            post_data["share_url"],
            post_data["thumbnail_url"],
        ]
        json_txt = folder_service.register_folder(*data)
        return json_txt.encode("UTF-8")

    if request.method == 'PUT':
        pass

    if request.method == 'DELETE':
        post_data = request.form
        folder_id = post_data["folder_id"]
        folder_service = FolderCommandService()
        ret = folder_service.delete_folder( folder_id )
        return ret.encode("UTF-8")
