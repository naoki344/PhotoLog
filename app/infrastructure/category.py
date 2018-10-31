# -*- coding: utf-8 -*-

from lib.model.category.category import AuthorID
from lib.model.category.category import DeleteStatus
from lib.model.category.category import Category
from lib.model.category.category import CategoryType
from lib.model.category.category import CategoryID
from lib.model.category.category_repository import CategoryRepository

from .datasource import DataSource


class CategoryDataSource(CategoryRepository):
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

        print(category_obj_list[0])
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
        sql = 'INSERT INTO {}_category(category_id,author_id,name,description,register_date,last_update_date,release_status,category_type,share_range,share_url,thumbnail_url,delete_status) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ;'.format(
            self.db_prefix)
        parameter = [
            category.category_id.value, category.author_id.value,
            category.name.value, category.description.value,
            category.register_date.value, category.last_update_date.value,
            category.release_status.name, category.category_type.name,
            category.share_range.name, category.share_url.value,
            category.thumbnail_url.value, category.delete_status.name
        ]
        category_id = self.datasource.insert(sql, parameter, True)

        return category_id

    def update(self, category: Category):
        sql = 'UPDATE {}_category SET author_id=%s,name=%s,description=%s,register_date=%s,last_update_date=%s,release_status=%s,category_type=%s,share_range=%s,share_url=%s,thumbnail_url=%s,delete_status=%s WHERE category_id=%s;'.format(
            self.db_prefix)
        parameter = [
            category.author_id.value, category.name.value,
            category.description.value, category.register_date.value,
            category.last_update_date.value, category.release_status.name,
            category.category_type.name, category.share_range.name,
            category.share_url.value, category.thumbnail_url.value,
            category.delete_status.name, category.category_id.value
        ]
        self.datasource.update(sql, parameter, True)
        category_id = category.category_id

        return self.find(category_id)

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
