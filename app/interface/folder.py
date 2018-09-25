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

@app_folder.route( '/', methods=['POST','GET'] )
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
        json_txt = folder_service.register_folder(post_data)
        return json_txt.encode("UTF-8")

#post_data = {
#    "author_ID" : 4,
#    "name" : "folder_name",
#    "description" : "memo",
#    "release_status" : 2,
#    "share_range" : 1,
#    "share_url" : "https://share_url.html",
#    "thumbnail_url" : "https://thumbnail_url.png",
#}
#{
#   folder_id : FolderID,
#   author_id : FolderAuthorID,
#   name : FolderName,
#   description : FolderDescription,
#   last_update_date : FolderLastUpdateDate,
#   register_date : FolderRegisterDate,
#   release_status : FolderReleaseStatus,
#   share_range : FolderShareRange,
#   share_url : FolderShareUrl,
#   thumbnail_url : FolderThumbnailUrl):
#}
        #folder = Folder('', 1, 'foldername', 'comment folder', datetime.datetime(2018, 9, 3, 22, 28, 49), datetime.datetime(2018, 9, 3, 22, 28, 49), 0, 0, 'https://share_url.html', 'https://thumbnail_url.png')
