# -*- coding: utf-8 -*-
import copy
from datetime import datetime
from abc import ABC
from abc import abstractmethod
from enum import Enum

from lib.model.content import Content
from lib.model.content import ContentID
from lib.model.info.info import Info
from lib.model.share.share import Share
'''
Value Object : ID
'''


class CategoryID(ContentID):
    def __init__(self, category_id: str):
        self.value = category_id


'''
Value Object : CategoryType
'''


class CategoryType(Enum):
    COMMON = 1
    ALBUM = 2


# カテゴリーを継承させるのであれば、CommonCategoryはCategory かつAlbumCategoryもCategoryでないといけない
# Is A の関係
# Has A の関係にしてはどうだろうか
#
# CommonCategoryもAlbumCategoryもカテゴリーです！！


class Category(Content, ABC):
    def __init__(self):
        pass

    @abstractmethod
    def to_dict(self):
        pass

    @staticmethod
    @abstractmethod
    def from_dict(dict_data: dict) -> 'Category':
        if dict_data['category_type'] == 'COMMON':
            return CommonCategory.from_dict(dict_data)
        if dict_data['category_type'] == 'ALBUM':
            return AlbumCategory.from_dict(dict_data)

    def get_content_id(self):
        return self.category_id

    def get_content_type(self):
        return 'Category'


class CommonCategory(Category):
    def __init__(self, category_id: CategoryID, category_type: CategoryType,
                 info: Info, share: Share):

        self.category_id = category_id
        self.category_type = category_type
        self.info = info
        self.share = share

    def to_dict(self):
        return {
            'category_id': self.category_id.value,
            'category_type': self.category_type.name,
            'info': self.info.to_dict(),
            'share': self.share.to_dict(),
        }

    def can_delete(self):
        return True

    def can_update(self):
        return True

    @staticmethod
    def from_dict(dict_data: dict) -> 'CommonCategory':
        return CommonCategory(
            category_id=CategoryID(dict_data["category_id"]),
            category_type=CategoryType[dict_data["category_type"]],
            info=Info.from_dict(dict_data),
            share=Share.from_dict(dict_data),
        )

    def modify(self, dict_data) -> 'CommonCategory':
        new_common_category = copy.deepcopy(self)

        if dict_data.get('info') is not None:
            new_common_category.info = self.info.modify(dict_data['info'])

        if dict_data.get('share') is not None:
            new_common_category.share = self.share.modify(dict_data['share'])

        return new_common_category


class AlbumCategory(Category):
    def __init__(self, category_id: CategoryID, category_type: CategoryType,
                 info: Info):

        self.category_id = category_id
        self.category_type = category_type
        self.info = info

    def to_dict(self):
        return {
            'category_id': self.category_id.value,
            'category_type': self.category_type.name,
            'info': self.info.to_dict(),
        }

    def can_delete(self):
        return True

    def can_update(self):
        return True

    @staticmethod
    def from_dict(dict_data: dict) -> 'AlbumCategory':
        return AlbumCategory(
            category_id=CategoryID(dict_data["category_id"]),
            category_type=CategoryType[dict_data["category_type"]],
            info=Info.from_dict(dict_data),
        )

    def modify(self, dict_data) -> 'AlbumCategory':
        new_album_category = copy.deepcopy(self)

        if dict_data.get('info') is not None:
            new_album_category.info = self.info.modify(dict_data['info'])

        return new_album_category
