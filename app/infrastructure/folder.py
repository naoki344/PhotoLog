# -*- coding: utf-8 -*-

from .datasource import DataSource
from lib.model.folder import Folder
from lib.model.folder import FolderAuthorID

class FolderDataSource():
    def __init__(self):
        self.datasource = DataSource()

    def get_all_folder(self, folder_author_id : FolderAuthorID ):
        sql = 'select * from folder WHERE author_id=%s'
        parameter = [folder_author_id]
        folders = self.datasource.get_db_data(sql, parameter)
        folder_obj_list = []
        for folder_data in folders :
            #Folder(1, None, 'name', '', datetime.datetime(2018, 9, 3, 22, 28, 49), datetime.datetime(2018, 9, 3, 22, 28, 49), 0, 0, '')
            folder_obj = Folder( *folder_data )
            folder_obj_list.append( folder_obj )

        return folder_obj_list
