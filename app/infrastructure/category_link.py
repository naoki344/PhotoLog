# -*- coding: utf-8 -*-

from lib.model.info.info import AuthorID
from lib.model.info.info import DeleteStatus
from lib.model.category.category import Category
from lib.model.category.category import CategoryType
from lib.model.category.category import CategoryID
from lib.model.folder.folder import FolderID
from lib.model.folder.folder import Folder
from lib.model.folder.folder_list import FolderList

from .datasource import DataSource


class CategoryFolderLinkDataSource:
    def __init__(self):
        self.datasource = DataSource()
        self.db_prefix = self.datasource.get_prefix()

    def find_linked_folder(self, category_id: CategoryID):
        sql = 'SELECT * FROM {}_category_folder_link INNER JOIN {}_folder ON {}_category_folder_link.folder_id = {}_folder.folder_id WHERE category_id=%s'.format(
            self.db_prefix,
            self.db_prefix,
            self.db_prefix,
            self.db_prefix,
        )
        parameter = [category_id.value]
        folders = self.datasource.get(sql, parameter, True)
        folder_obj_list = []
        for folder_row in folders:
            folder_obj = self._to_folder_obj(folder_row)
            folder_obj_list.append(folder_obj)

        folder_list = FolderList(folder_obj_list)
        return folder_list

    def link_folder(self, category_id: CategoryID, folder_id: FolderID):
        sql = 'INSERT INTO {}_category_folder_link(category_id,folder_id) VALUES(%s,%s) ;'.format(
            self.db_prefix)

        parameter = [
            category_id.value,
            folder_id.value,
        ]
        self.datasource.insert(sql, parameter, True)
        return True

    def unlink_folder(self, category_id: CategoryID, folder_id: FolderID):
        sql = 'DELETE FROM {}_category_folder_link WHERE category_id=%s AND folder_id=%s'.format(
            self.db_prefix)

        parameter = [
            category_id.value,
            folder_id.value,
        ]
        try:
            self.datasource.update(sql, parameter, True)
        except:
            raise

        return True

    def _to_folder_obj(self, folder_row):
        folder_obj = Folder.from_dict(folder_row)
        return folder_obj
