# -*- coding: utf-8 -*-

from lib.model.info.info import AuthorID
from lib.model.info.info import DeleteStatus
from lib.model.category.category import Category
from lib.model.category.category import CategoryType
from lib.model.category.category import CategoryID

from .datasource import DataSource


class CategoryDataSource:
    def __init__(self):
        self.datasource = DataSource()
        self.db_prefix = self.datasource.get_prefix()

    def find_user_all(self, author_id: AuthorID, category_type: CategoryType):
        sql = 'SELECT * FROM {}_category WHERE author_id=%s AND delete_status="UNDELETED" AND category_type=%s;'.format(
            self.db_prefix)
        parameter = [author_id.value, category_type.name]
        categories = self.datasource.get(sql, parameter, True)
        category_obj_list = []
        for category_row in categories:
            category_obj = self._to_category_obj(category_row)
            category_obj_list.append(category_obj)

        return category_obj_list

    def find(self, category_id: CategoryID):
        sql = 'SELECT * FROM {}_category WHERE category_id=%s;'.format(
            self.db_prefix)
        parameter = [category_id.value]
        categorys = self.datasource.get(sql, parameter, True)
        if len(categorys) == 0:
            return None

        category_row = categorys[0]
        category_obj = self._to_category_obj(category_row)
        return category_obj

    def register(self, category: Category):
        sql = 'INSERT INTO {}_category(category_id,category_type,author_id,name,description,register_date,last_update_date,release_status,thumbnail_url,delete_status,share_range,share_password) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ;'.format(
            self.db_prefix)

        if category.category_type is CategoryType.COMMON:
            parameter = [
                category.category_id.value,
                category.category_type.name,
                category.info.author_id.value,
                category.info.name.value,
                category.info.description.value,
                category.info.register_date.value,
                category.info.last_update_date.value,
                category.info.release_status.name,
                category.info.thumbnail_url.value,
                category.info.delete_status.name,
                category.share.share_range.name,
                category.share.share_password.value,
            ]
            category_id = self.datasource.insert(sql, parameter, True)
            return category_id

        if category.category_type is CategoryType.ALBUM:
            parameter = [
                category.category_id.value,
                category.category_type.name,
                category.info.author_id.value,
                category.info.name.value,
                category.info.description.value,
                category.info.register_date.value,
                category.info.last_update_date.value,
                category.info.release_status.name,
                category.info.thumbnail_url.value,
                category.info.delete_status.name,
                '',
                '',
            ]
            category_id = self.datasource.insert(sql, parameter, True)
            return category_id

        return False

    def update(self, category: Category):
        sql = 'UPDATE {}_category SET category_type=%s,author_id=%s,name=%s,description=%s,register_date=%s,last_update_date=%s,release_status=%s,thumbnail_url=%s,delete_status=%s,share_range=%s,share_password=%s WHERE category_id=%s;'.format(
            self.db_prefix)
        if category.category_type is CategoryType.COMMON:
            parameter = [
                category.category_type.name,
                category.info.author_id.value,
                category.info.name.value,
                category.info.description.value,
                category.info.register_date.value,
                category.info.last_update_date.value,
                category.info.release_status.name,
                category.info.thumbnail_url.value,
                category.info.delete_status.name,
                category.share.share_range.name,
                category.share.share_password.value,
                category.category_id.value,
            ]
            self.datasource.update(sql, parameter, True)
            category_id = category.category_id
            return self.find(category_id)

        if category.category_type is CategoryType.ALBUM:
            parameter = [
                category.category_type.name,
                category.info.author_id.value,
                category.info.name.value,
                category.info.description.value,
                category.info.register_date.value,
                category.info.last_update_date.value,
                category.info.release_status.name,
                category.info.thumbnail_url.value,
                category.info.delete_status.name,
                '',
                '',
                category.category_id.value,
            ]
            self.datasource.update(sql, parameter, True)
            category_id = category.category_id
            return self.find(category_id)

        return False

    def delete(self, category: Category):
        category_id = category.category_id.value
        sql = 'UPDATE {}_category SET delete_status="DELETED" WHERE category_id=%s;'.format(
            self.db_prefix)
        parameter = [category_id]
        try:
            ret_status = self.datasource.update(sql, parameter, True)
        except:
            raise

        return True

    def _to_category_obj(self, category_row):
        category_obj = Category.from_dict(category_row)
        return category_obj
