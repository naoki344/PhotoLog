# -*- coding: utf-8 -*-

import json

from flask import Blueprint, request

from app.application.folder import FolderCommandService, FolderQueryService
from lib.model.folder.folder import Folder, FolderAuthorID
from lib.model.folder.folder_factory import FolderFactory

app_folder = Blueprint('app_folder', __name__)

#main で登録されているPATHからの相対パスで以下のURLを指定する
#  以下の場合のPATHは、/photo_log/folder/file になる
#  - main.py のregister_blueprint が url_prefix='/photo_log/folder'
#  - @app_folder.route('/file')


@app_folder.route('/', methods=['GET', 'POST'])
def folder_index(user_id):
    folder_author_id = user_id
    if request.method == 'GET':
        folder_query_service = FolderQueryService()
        user_folder_list = folder_query_service.find_user_all(folder_author_id)
        folder_dict_list = user_folder_list.to_dict()
        json_txt = json.dumps(folder_dict_list, indent=4)
        return json_txt.encode("UTF-8")

    if request.method == 'POST':
        post_data = request.form
        recive_data = _to_folder_dict(post_data)

        folder_factory = FolderFactory()
        folder_obj = folder_factory.create(recive_data)

        folder_command_service = FolderCommandService()
        registerd_folder = folder_command_service.register(folder_obj)

        folder_dict = registerd_folder.to_dict()
        json_txt = json.dumps(folder_dict, indent=4)
        return json_txt.encode("UTF-8")


@app_folder.route('/<path:folder_id>', methods=['GET', 'PUT', 'DELETE'])
def folder(user_id, folder_id):
    folder_author_id = user_id
    if request.method == 'GET':
        folder_query_service = FolderQueryService()
        folder_obj = folder_query_service.find(folder_id)
        if folder_obj == None:
            txt = 'folder do not exist'
            return txt.encode("UTF-8")

        folder_dict = folder_obj.to_dict()
        json_txt = json.dumps(folder_dict, indent=4)
        return json_txt.encode("UTF-8")

    if request.method == 'PUT':
        post_data = request.form
        recive_data = _to_folder_dict(post_data)

        folder_factory = FolderFactory()
        new_folder = folder_factory.restore(recive_data)

        folder_query_service = FolderQueryService()
        org_folder = folder_query_service.find(folder_id)
        if folder_obj == None:
            txt = 'folder do not exist'
            return txt.encode("UTF-8")

        folder_command_service = FolderCommandService()
        updated_folder = folder_command_service.update(org_folder, new_folder)

        folder_dict = updated_folder.to_dict()
        json_txt = json.dumps(folder_dict, indent=4)
        return json_txt.encode("UTF-8")

    if request.method == 'DELETE':
        post_data = request.form

        folder_query_service = FolderQueryService()
        org_folder = folder_query_service.find(folder_id)

        folder_command_service = FolderCommandService()
        deleted_folder = folder_command_service.delete(org_folder)

        json_txt = json.dumps(deleted_folder, indent=4)
        return json_txt.encode("UTF-8")


def _to_folder_dict(post_data) -> Folder:
    data = {}
    if post_data.get('folder_id') == None:
        data['folder_id'] = ''
    else:
        data['folder_id'] = post_data['folder_id']

    if post_data.get('delete_flag') == None:
        data['delete_flag'] = 0
    else:
        data['delete_flag'] = post_data['delete_flag']

    data['author_id'] = post_data['author_id']
    data['name'] = post_data['name']
    data['description'] = post_data['description']
    data['release_status'] = post_data['release_status']
    data['share_range'] = post_data['share_range']
    data['share_url'] = post_data['share_url']
    data['thumbnail_url'] = post_data['thumbnail_url']

    dict_data = {
        "folder_id": data["folder_id"],
        "author_id": data["author_id"],
        "name": data["name"],
        "description": data["description"],
        "release_status": int(data["release_status"]),
        "share_range": int(data["share_range"]),
        "share_url": data["share_url"],
        "thumbnail_url": data["thumbnail_url"],
        "delete_flag": int(data["delete_flag"]),
    }
    return dict_data
