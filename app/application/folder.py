# -*- coding: utf-8 -*-

import sys,os
#sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
from app.infrastructure.folder import FolderDataSource
from lib.model.folder.user_folder_list import UserFolderList
from lib.model.folder.folder import FolderAuthorID

class GetUserAllFolderService():

    def __init__( self, folder_author_id : FolderAuthorID ):
        folderdata = FolderDataSource()
        folders = folderdata.get_all_folder(folder_author_id)
        self.user_folder_list = UserFolderList(folders)

    def get_all_folder(self):
        return self.user_folder_list
