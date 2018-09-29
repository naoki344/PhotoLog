# -*- coding: utf-8 -*-

import json

from flask import Blueprint
from flask import request

from app.application.folder import FolderCommandService
from app.application.folder import FolderQueryService
from lib.model.folder.folder import Folder
from lib.model.folder.folder import FolderAuthorID
from lib.model.folder.folder import FolderFactories

app_folder = Blueprint('app_folder', __name__)

#main で登録されているPATHからの相対パスで以下のURLを指定する
#  以下の場合のPATHは、/photo_log/folder/file になる
#  - main.py のregister_blueprint が url_prefix='/photo_log/folder'
#  - @app_folder.route('/file')


@app_folder.route('/', methods=['POST', 'GET', 'PUT', 'DELETE'])
def folder_index():
    if request.method == 'GET':
        folder_author_id = 1
        folder_service = FolderQueryService()
        json_txt = folder_service.find_all_folder(folder_author_id)
        return json_txt.encode("UTF-8")

    if request.method == 'POST':
        post_data = request.form
        recive_data = _to_folder_dict(post_data)

        folder_factories = FolderFactories()
        folder_obj = folder_factories.create_folder(recive_data)

        folder_service = FolderCommandService()
        registerd_folder = folder_service.register_folder(folder_obj)
        folder_dict = registerd_folder.to_dict()
        json_txt = json.dumps(folder_dict, indent=4)
        return json_txt.encode("UTF-8")

    if request.method == 'PUT':
        post_data = request.form
        recive_data = _to_folder_dict(post_data)

        folder_query_service = FolderQueryService()
        folder = folder_query_service.find_folder(recive_data["folder_id"])
        if (folder.can_update()):
            folder_command_service = FolderCommandService()
            updated_folder = folder_command_service.update_folder(
                folder, recive_data)
            folder_dict = updated_folder.to_dict()
        json_txt = json.dumps(folder_dict, indent=4)
        return json_txt.encode("UTF-8")

    if request.method == 'DELETE':
        post_data = request.form
        folder_id = post_data["folder_id"]
        folder_service = FolderCommandService()
        ret = folder_service.delete_folder(folder_id)
        return ret.encode("UTF-8")


def _to_folder_dict(self, post_data) -> Folder:
    data = [
        post_data["folder_id"],
        post_data["author_id"],
        post_data["name"],
        post_data["description"],
        post_data["release_status"],
        post_data["share_range"],
        post_data["share_url"],
        post_data["thumbnail_url"],
        post_data["delete_flag"],
    ]
    return data
