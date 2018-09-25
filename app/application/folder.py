# -*- coding: utf-8 -*-

import sys,os
import json
import datetime
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../..')
from app.infrastructure.folder import FolderDataSource
from lib.model.folder.folder_list import FolderList
from lib.model.folder.folder import Folder
from lib.model.folder.folder import FolderID
from lib.model.folder.folder import FolderAuthorID

class FolderQueryService():

    def __init__( self ):
        self.folder_datasource = FolderDataSource()

    def find_all_folder(self, folder_author_id : FolderAuthorID ):
        folders = self.folder_datasource.get_all_folder(folder_author_id)
        user_folder_list = FolderList(folders)
        folder_dict_list = user_folder_list.to_dict()
        json_txt = json.dumps( folder_dict_list ,indent=4)
        return json_txt

    def find_folder(self, folder_id : FolderID ):
        pass


class FolderCommandService():

    def __init__( self ):
        self.folder_datasource = FolderDataSource()

    def register_folder(self,
        author_id,
        name,
        description,
        release_status,
        share_range,
        share_url,
        thumbnail_url ):

        folder = Folder(
            '',
            int(author_id),
            name,
            description,
            '',
            '',
            int(release_status),
            int(share_range),
            share_url,
            thumbnail_url,
            0 )
        folder_obj = self.folder_datasource.register_folder( folder )
        folder_dict = folder_obj.to_dict()
        json_txt = json.dumps( folder_dict ,indent=4)
        return json_txt
