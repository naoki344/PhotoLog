# -*- coding: utf-8 -*-

import datetime
import json
import os
import sys

from app.infrastructure.folder import FolderDataSource
from lib.model.folder.folder import Folder, FolderAuthorID, FolderID
from lib.model.folder.folder_list import FolderList

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../..')


class FolderQueryService():
    def __init__(self):
        self.folder_datasource = FolderDataSource()

    def find_all_folder(self, folder_author_id: FolderAuthorID):
        folders = self.folder_datasource.get_all_folder(folder_author_id)
        user_folder_list = FolderList(folders)
        folder_dict_list = user_folder_list.to_dict()
        json_txt = json.dumps(folder_dict_list, indent=4)
        return json_txt

    def find_folder(self, folder_id: FolderID):
        folder_obj = self.folder_datasource.find_folder(folder_id)
        folder_dict = folder_obj.to_dict()
        json_txt = json.dumps(folder_dict, indent=4)


class FolderCommandService():
    def __init__(self):
        self.folder_datasource = FolderDataSource()

    def register_folder(self, folder: Folder):
        folder_obj = self.folder_datasource.register_folder(folder)
        return folder_obj

    def update_folder(self, folder: Folder):
        folder_obj = self.folder_datasource.update_folder(folder)
        folder_dict = folder_obj.to_dict()
        json_txt = json.dumps(folder_dict, indent=4)
        return json_txt

    def delete_folder(self, folder_id):
        try:
            folder_obj = self.folder_datasource.delete_folder(int(folder_id))
        except:
            msg = 'folder[' + folder_id + '] delete is failuer'
            return msg

        return folder_id
