# -*- coding: utf-8 -*-

import sys,os
#sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
from app.infrastructure.folder import FolderDataSource
from lib.model.folder import FolderAuthorID

class GetAllFolderService():

    def __init__( self, folder_author_id : FolderAuthorID ):
        folderdata = FolderDataSource()
        self.folders = folderdata.get_all_folder(folder_author_id)

