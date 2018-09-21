# -*- coding: utf-8 -*-

from app.application.folder import GetUserAllFolderService
from lib.model.folder.folder import FolderAuthorID
from flask import Blueprint


app_folder = Blueprint('app_folder',__name__)

@app_folder.route('/')
def folder_index():
    folder_author_id = 1
    folder_service = GetUserAllFolderService(folder_author_id)
    json_txt = folder_service.get_all_folder()
    return json_txt.encode("UTF-8")
