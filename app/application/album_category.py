# -*- coding: utf-8 -*-

import datetime
import json
import os
import sys

from app.infrastructure.category import CategoryDataSource
from app.infrastructure.album_content import AlbumContentDataSource
from lib.model.album.album import AlbumID
from lib.model.category.category import AuthorID
from lib.model.category.category import AlbumCategory
from lib.model.category.category import CategoryID
from lib.model.category.category import CategoryType
from lib.model.category.category_list import CategoryList

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../..')


class AlbumCategoryQueryService:
    def __init__(self):
        self.album_category_datasource = CategoryDataSource()
        self.album_content_datasource = AlbumContentDataSource()

    def find_user_all(self, author_id: AuthorID):
        album_categorys = self.album_category_datasource.find_user_all(
            author_id, CategoryType['ALBUM'])
        user_album_category_list = CategoryList(album_categorys)
        return user_album_category_list

    def find(self, album_category_id: CategoryID):
        album_category = self.album_category_datasource.find(album_category_id)
        if album_category == None:
            return None
        return album_category


class AlbumCategoryCommandService:
    def __init__(self):
        self.album_category_datasource = CategoryDataSource()

    def register(self, album_category: AlbumCategory, album_id: AlbumID):
        self.album_category_datasource.register(album_category)
        # album_contentに登録する
        self.album_content_datasource.register(AlbumID, AlbumCategory)
        return album_category

    def update(self, org_album_category: AlbumCategory,
               new_album_category: AlbumCategory):
        if org_album_category.can_update():
            updated_album_category = self.album_category_datasource.update(
                new_album_category)
        return updated_album_category

    def delete(self, album_category: AlbumCategory):
        if album_category.can_delete():
            deleted_album_category = self.album_category_datasource.delete(
                album_category)
            self.album_content_datasource.delete(AlbumID, AlbumCategory)
        return deleted_album_category
