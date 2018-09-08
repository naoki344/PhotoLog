# -*- coding: utf-8 -*-

from datasource import DataSource

class FolderDataSource():
    def __init__(self):
        self.datasource = DataSource()

    def get_all_folder(self):
        sql = 'select * from folder'
        parameter = ()
        folders = self.datasource.get_db_data(sql, parameter)
        print ( folders )


fd = FolderDataSource()
fd.get_all_folder()
