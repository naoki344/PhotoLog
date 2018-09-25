# -*- coding: utf-8 -*-

from .datasource import DataSource
from lib.model.folder.folder import Folder
from lib.model.folder.folder import FolderAuthorID

class FolderDataSource():
    def __init__(self):
        self.datasource = DataSource()

    def get_all_folder(self, folder_author_id : FolderAuthorID ):
        sql = 'SELECT * FROM folder WHERE author_id=%s;'
        parameter = [folder_author_id]
        folders = self.datasource.get_db_data(sql, parameter)
        folder_obj_list = []
        for folder_data in folders :
            folder_obj = Folder( *folder_data )
            folder_obj_list.append( folder_obj )

        return folder_obj_list


    def register_folder(self, folder : Folder ):
        sql = 'INSERT INTO folder(author_id,name,description,release_status,share_range,share_url,thumbnail_url) VALUES(%s,%s,%s,%s,%s,%s,%s) ;'
        parameter = [
            folder.author_id.value,
            folder.name.value,
            folder.description.value,
            folder.release_status.value,
            folder.share_range.value,
            folder.share_url.value,
            folder.thumbnail_url.value
        ]
        folder_id = self.datasource.insert_db(sql, parameter)

        sql = 'SELECT * FROM folder WHERE folder_ID=%s'
        parameter = [folder_id]
        data = self.datasource.get_db_data(sql, parameter)
        folder_row = data[0]
        folder_obj = Folder( *folder_row )
        return folder_obj
