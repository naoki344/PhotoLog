# -*- coding: utf-8 -*-

import datetime
import json
import os
import sys

from app.infrastructure.folder import FolderDataSource
from lib.model.folder.folder import Folder
from lib.model.folder.folder import FolderAuthorID
from lib.model.folder.folder import FolderID
from lib.model.folder.folder_list import FolderList

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../..')


class FolderQueryService():
    def __init__(self):
        self.folder_datasource = FolderDataSource()

    def find_user_all(self, folder_author_id: FolderAuthorID):
        folders = self.folder_datasource.find_user_all(folder_author_id)
        user_folder_list = FolderList(folders)
        return user_folder_list

    def find(self, folder_id: FolderID):
        folder = self.folder_datasource.find(folder_id)
        if folder == None:
            return None
        return folder


class FolderCommandService():
    def __init__(self):
        self.folder_datasource = FolderDataSource()

    def register(self, folder: Folder):
        result = self.folder_datasource.register(folder)
        return folder

    def update(self, org_folder: Folder, new_folder: Folder):
        if org_folder.can_update() :
            updated_folder = self.folder_datasource.update(new_folder)
        return updated_folder

    def delete(self, folder: Folder):
        if folder.can_delete() :
            try:
                deleted_folder = self.folder_datasource.delete(folder)
            except:
                msg = 'folder[' + folder.folder_id.value + '] delete is failuer'
                return msg

        return deleted_folder
