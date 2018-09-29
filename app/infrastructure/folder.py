# -*- coding: utf-8 -*-

from lib.model.folder.folder import (Folder, FolderAuthorID, FolderDeleteFlag,
                                     FolderID)
from lib.model.folder.folder_repository import FolderRepository

from .datasource import DataSource


class FolderDataSource(FolderRepository):
    def __init__(self):
        self.datasource = DataSource()

    def get_all_folder(self, folder_author_id: FolderAuthorID):
        sql = 'SELECT * FROM folder WHERE author_id=%s AND delete_flag=0;'
        parameter = [folder_author_id]
        folders = self.datasource.get(sql, parameter, True)
        folder_obj_list = []
        for folder_row in folders:
            folder_obj = self._to_folder_obj(folder_row)
            folder_obj_list.append(folder_obj)

        return folder_obj_list

    def find_folder(self, folder_id: FolderID):
        sql = 'SELECT * FROM folder WHERE folder_id=%s;'
        parameter = [folder_id]
        folders = self.datasource.get(sql, parameter, True)
        folder_row = folders[0]

        if folder_row == '':
            return ''
        folder_obj = self._to_folder_obj(folder_row)
        return folder_obj

    def register_folder(self, folder: Folder):
        sql = 'INSERT INTO folder(author_id,name,description,release_status,share_range,share_url,thumbnail_url) VALUES(%s,%s,%s,%s,%s,%s,%s) ;'
        parameter = [
            folder.author_id.value, folder.name.value,
            folder.description.value, folder.release_status.value,
            folder.share_range.value, folder.share_url.value,
            folder.thumbnail_url.value
        ]
        folder_id = self.datasource.insert(sql, parameter, True)

        sql = 'SELECT * FROM folder WHERE folder_ID=%s'
        parameter = [folder_id]
        folders = self.datasource.get(sql, parameter, True)
        folder_row = folders[0]
        folder_obj = self._to_folder_obj(folder_row)
        return folder_obj

    def update_folder(self, folder: Folder):
        sql = 'UPDATE folder SET author_id=%s,name=%s,description=%s,release_status=%s,share_range=%s,share_url=%s,thumbnail_url=%s WHERE folder_id=%s;'
        parameter = [
            folder.author_id.value, folder.name.value,
            folder.description.value, folder.release_status.value,
            folder.share_range.value, folder.share_url.value,
            folder.thumbnail_url.value, folder.folder_id.value
        ]
        self.datasource.update(sql, parameter, True)
        folder_id = folder.folder_id.value

        sql = 'SELECT * FROM folder WHERE folder_id=%s'
        parameter = [folder_id]
        folders = self.datasource.get(sql, parameter, True)
        folder_row = folders[0]
        folder_obj = self._to_folder_obj(folder_row)
        return folder_obj

    def delete_folder(self, folder_id: FolderID):
        del_flag = FolderDeleteFlag.DELETED.value
        sql = 'UPDATE folder SET delete_flag=%s WHERE folder_id=%s;'
        parameter = [del_flag, folder_id]
        try:
            ret_status = self.datasource.update(sql, parameter, True)
        except:
            raise

        return True

    def _to_folder_obj(self, folder_row):
        folder_obj = Folder(
            folder_row["folder_id"],
            folder_row["author_id"],
            folder_row["name"],
            folder_row["description"],
            folder_row["register_date"],
            folder_row["last_update_date"],
            folder_row["release_status"],
            folder_row["share_range"],
            folder_row["share_url"],
            folder_row["thumbnail_url"],
            folder_row["delete_flag"],
        )
        return folder_obj
