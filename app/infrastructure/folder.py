# -*- coding: utf-8 -*-

from lib.model.info.info import AuthorID
from lib.model.info.info import DeleteStatus
from lib.model.folder.folder import Folder
from lib.model.folder.folder import FolderID

from .datasource import DataSource


class FolderDataSource():
    def __init__(self):
        self.datasource = DataSource()
        self.db_prefix = self.datasource.get_prefix()

    def find_user_all(self, author_id: AuthorID):
        sql = 'SELECT * FROM {}_folder WHERE author_id=%s AND delete_status="UNDELETED";'.format(
            self.db_prefix)
        parameter = [author_id.value]
        folders = self.datasource.get(sql, parameter, True)
        folder_obj_list = []
        for folder_row in folders:
            folder_obj = self._to_folder_obj(folder_row)
            folder_obj_list.append(folder_obj)

        return folder_obj_list

    def find(self, folder_id: FolderID):
        sql = 'SELECT * FROM {}_folder WHERE folder_id=%s;'.format(
            self.db_prefix)
        parameter = [folder_id.value]
        folders = self.datasource.get(sql, parameter, True)
        if len(folders) == 0:
            return None

        folder_row = folders[0]
        folder_obj = self._to_folder_obj(folder_row)
        return folder_obj

    def register(self, folder: Folder):
        sql = 'INSERT INTO {}_folder(folder_id,author_id,name,description,register_date,last_update_date,release_status,thumbnail_url,delete_status,share_range,share_password) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ;'.format(
            self.db_prefix)
        parameter = [
            folder.folder_id.value,
            folder.info.author_id.value,
            folder.info.name.value,
            folder.info.description.value,
            folder.info.register_date.value,
            folder.info.last_update_date.value,
            folder.info.release_status.name,
            folder.info.thumbnail_url.value,
            folder.info.delete_status.name,
            folder.share.share_range.name,
            folder.share.share_password.value,
        ]
        folder_id = self.datasource.insert(sql, parameter, True)

        return True

    def update(self, folder: Folder):
        sql = 'UPDATE {}_folder SET author_id=%s,name=%s,description=%s,register_date=%s,last_update_date=%s,release_status=%s,share_range=%s,share_url=%s,thumbnail_url=%s,delete_status=%s WHERE folder_id=%s;'.format(
            self.db_prefix)
        parameter = [
            folder.info.author_id.value, folder.info.name.value,
            folder.info.description.value, folder.info.register_date.value,
            folder.info.last_update_date.value,
            folder.info.release_status.name, folder.info.thumbnail_url.value,
            folder.share.share_range.name, folder.share.share_url.value,
            folder.info.delete_status.name, folder.folder_id.value
        ]
        self.datasource.update(sql, parameter, True)
        folder_id = folder.folder_id

        return self.find(folder_id)

    def delete(self, folder: Folder):
        folder_id = folder.folder_id.value
        sql = 'UPDATE {}_folder SET delete_status="DELETED" WHERE folder_id=%s;'.format(
            self.db_prefix)
        parameter = [folder_id]
        try:
            ret_status = self.datasource.update(sql, parameter, True)
        except:
            raise

        return True

    def _to_folder_obj(self, folder_row):
        folder_obj = Folder.from_dict(folder_row)
        return folder_obj
