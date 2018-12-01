# -*- coding: utf-8 -*-

import time
import uuid
from datetime import datetime
from abc import ABC
from abc import ABCMeta, abstractmethod

from lib.model.category.category import Category
from lib.model.category.category import CommonCategory
from lib.model.category.category import AlbumCategory
from lib.model.category.category import Category
from lib.model.category.category import CategoryID
from lib.model.category.category import CategoryType
from lib.model.info.info_factory import InfoFactory
from lib.model.share.share_factory import ShareFactory


class CategoryFactory(metaclass=ABCMeta):
    @staticmethod
    def create(dict_data) -> Category:
        if dict_data.get('category_type') is None:
            return False
        if dict_data['category_type'] == CategoryType.COMMON_CATEGORY.name:
            return CommonCategoryFactory.create(dict_data)
        if dict_data['category_type'] == CategoryType.ALBUM_CATEGORY.name:
            return AlbumCategoryFactory.create(dict_data)

    @staticmethod
    def _to_category_obj(dict_data):
        pass


class CommonCategoryFactory(CategoryFactory):
    @staticmethod
    def create(dict_data) -> CommonCategory:
        if dict_data.get('category_type') is None:
            return False

        if dict_data.get('category_id') is None:
            if dict_data['category_type'] != CategoryType.COMMON_CATEGORY.name:
                return False
            dict_data['category_id'] = 'common_category-' + str(uuid.uuid4())

        if dict_data.get('info') is None:
            return False

        if dict_data.get('share') is None:
            return False

        return CommonCategoryFactory._to_category_obj(dict_data)

    @staticmethod
    def _to_category_obj(dict_data):
        return CommonCategory(
            category_id=CategoryID(dict_data["category_id"]),
            category_type=CategoryType[dict_data["category_type"]],
            info=InfoFactory.create(dict_data['info']),
            share=ShareFactory.create(dict_data['share']),
        )


class AlbumCategoryFactory(CategoryFactory):
    @staticmethod
    def create(dict_data) -> AlbumCategory:
        if dict_data.get('category_type') is None:
            return False

        if dict_data.get('category_id') is None:
            if dict_data['category_type'] != CategoryType.ALBUM_CATEGORY.name:
                return False
            dict_data['category_id'] = 'album_category-' + str(uuid.uuid4())

        if dict_data.get('info') is None:
            return False

        return AlbumCategoryFactory._to_category_obj(dict_data)

    @staticmethod
    def _to_category_obj(dict_data):
        return AlbumCategory(
            category_id=CategoryID(dict_data["category_id"]),
            category_type=CategoryType[dict_data["category_type"]],
            info=InfoFactory.create(dict_data['info']),
        )
