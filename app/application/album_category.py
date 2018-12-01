# -*- coding: utf-8 -*-

import datetime
import json
import os
import sys

from lib.model.info.info import AuthorID
from app.infrastructure.category import CategoryDataSource
from app.application.album_content import AlbumContentCommandService
from app.application.album_content import AlbumContentQueryService
from lib.model.album.album import AlbumID
from lib.model.album_content.album_content_factory import AlbumContentFactory
from lib.model.category.category import AlbumCategory
from lib.model.category.category import CategoryID
from lib.model.category.category import CategoryType
from lib.model.category.category_list import CategoryList

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../..')


class AlbumCategoryQueryService:
    def __init__(self):
        self.album_category_datasource = CategoryDataSource()

    def find_user_all(self, author_id: AuthorID):
        album_categorys = self.album_category_datasource.find_user_all(
            author_id, CategoryType['ALBUM_CATEGORY'])
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
        self.album_content_command_service = AlbumContentCommandService()
        self.album_content_query_service = AlbumContentQueryService()

    def register(self, album_id: AlbumID, album_category: AlbumCategory):
        self.album_category_datasource.register(album_category)
        # album_contentに登録する
        # albumcontentを渡すようにする
        data = {}
        data['album_id'] = album_id
        data['content'] = album_category
        album_content_factory = AlbumContentFactory()
        album_content = album_content_factory.create(data)
        self.album_content_command_service.register(album_content)

    def update(self, org_album_category: AlbumCategory,
               new_album_category: AlbumCategory):
        if org_album_category.can_update():
            self.album_category_datasource.update(new_album_category)
            return True
        return False

    def delete(self, album_id: AlbumID, album_category: AlbumCategory):
        if album_category.can_delete() is False:
            return False
        self.album_category_datasource.delete(album_category)
        album_content = self.album_content_query_service.find(
            album_id, album_category.category_id)
        # albumcontentを渡すようにする
        self.album_content_command_service.delete(album_content)
        return True
