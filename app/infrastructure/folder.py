# -*- coding: utf-8 -*-

from lib.model.folder.folder import (Folder, FolderAuthorID, FolderDeleteFlag,
                                     FolderID)
from lib.model.folder.folder_repository import FolderRepository

from .datasource import DataSource


class FolderDataSource(FolderRepository):
    def __init__(self):
        self.datasource = DataSource()

    def find_user_all(self, folder_author_id: FolderAuthorID):
        sql = 'SELECT * FROM folder WHERE author_id=%s AND delete_status="UNDELETED";'
        parameter = [folder_author_id]
        folders = self.datasource.get(sql, parameter, True)
        folder_obj_list = []
        for folder_row in folders:
            print(folder_row)
            folder_obj = self._to_folder_obj(folder_row)
            folder_obj_list.append(folder_obj)

        return folder_obj_list

    def find(self, folder_id: FolderID):
        sql = 'SELECT * FROM folder WHERE folder_id=%s;'
        parameter = [folder_id]
        folders = self.datasource.get(sql, parameter, True)
        if len(folders) == 0:
            return None

        folder_row = folders[0]
        folder_obj = self._to_folder_obj(folder_row)
        return folder_obj

    def register(self, folder: Folder):
        sql = 'INSERT INTO folder(folder_id,author_id,name,description,register_date,last_update_date,release_status,share_range,share_url,thumbnail_url,delete_status) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ;'
        parameter = [
            folder.folder_id.value, folder.author_id.value, folder.name.value,
            folder.description.value, folder.register_date.value,
            folder.last_update_date.value, folder.release_status.name,
            folder.share_range.name, folder.share_url.value,
            folder.thumbnail_url.value, folder.delete_flag.name
        ]
        folder_id = self.datasource.insert(sql, parameter, True)

        return True

    def update(self, folder: Folder):
        sql = """UPDATE folder SET author_id=%s,name=%s,description=%s,register_date=%s,last_update_date=%s,release_status=%s,share_range=%s,share_url=%s,thumbnail_url=%s,delete_status=%s WHERE folder_id=%s;"""
        parameter = [
            folder.author_id.value, folder.name.value,
            folder.description.value, folder.register_date.value,
            folder.last_update_date.value, folder.release_status.name,
            folder.share_range.name, folder.share_url.value,
            folder.thumbnail_url.value, folder.delete_flag.name,
            folder.folder_id.value
        ]
        folder_id = folder.folder_id.value
        self.datasource.update(sql, parameter, True)
        folder_id = folder.folder_id.value
        print(folder_id)

        sql = 'SELECT * FROM folder WHERE folder_id=%s'
        parameter = [folder_id]
        folders = self.datasource.get(sql, parameter, True)
        folder_row = folders[0]
        folder_obj = self._to_folder_obj(folder_row)
        return folder_obj

    def delete(self, folder: Folder):
        folder_id = folder.folder_id.value
        #del_flag = FolderDeleteFlag.DELETED.name
        sql = 'UPDATE folder SET delete_status="DELETED" WHERE folder_id=%s;'
        parameter = [folder_id]
        try:
            ret_status = self.datasource.update(sql, parameter, True)
        except:
            raise

        return True

    def _to_folder_obj(self, folder_row):
        folder_obj = Folder.from_dict(folder_row)
        return folder_obj
