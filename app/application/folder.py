# -*- coding: utf-8 -*-

import sys,os
#sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
from app.infrastructure.folder import FolderDataSource
from lib.model.folder.folder_list import FolderList
from lib.model.folder.folder import FolderAuthorID

class GetUserAllFolderService():

    def __init__( self, folder_author_id : FolderAuthorID ):
        self.folder_author_id = folder_author_id
        self.folder_datasource = FolderDataSource()

    def get_all_folder(self):
        folders = self.folder_datasource.get_all_folder(self.folder_author_id)
        user_folder_list = FolderList(folders)
        json_txt = user_folder_list.to_dict()
        return json_txt
