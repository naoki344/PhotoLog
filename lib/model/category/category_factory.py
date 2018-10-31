# -*- coding: utf-8 -*-

import time
import uuid
from datetime import datetime

from lib.model.category.category import AuthorID
from lib.model.category.category import DeleteStatus
from lib.model.category.category import Description
from lib.model.category.category import Category
from lib.model.category.category import CommonCategory
from lib.model.category.category import AlbumCategory
from lib.model.category.category import CategoryID
from lib.model.category.category import CategoryType
from lib.model.category.category import LastUpdateDate
from lib.model.category.category import Name
from lib.model.category.category import RegisterDate
from lib.model.category.category import ReleaseStatus
from lib.model.category.category import ShareRange
from lib.model.category.category import ShareUrl
from lib.model.category.category import ThumbnailUrl


class CategoryFactory():
    def create(self, dict_data) -> Category:
        now_time = datetime.now()

        if dict_data.get('category_id') is None:
            dict_data['category_id'] = 'category-' + str(uuid.uuid4())

        if dict_data.get('author_id') is None:
            return False

        if dict_data.get('name') is None:
            return False

        if dict_data.get('description') is None:
            dict_data['description'] = ''

        if dict_data.get('register_date') is None:
            dict_data['register_date'] = now_time

        if dict_data.get('last_update_date') is None:
            dict_data['last_update_date'] = now_time

        if dict_data.get('release_status') is None:
            dict_data['release_status'] = 'OPEN'

        if dict_data.get('category_type') is None:
            return False

        if dict_data.get('share_range') is None:
            dict_data['share_range'] = 'PRIVATE'

        if dict_data.get('share_url') is None:
            dict_data['share_url'] = ''

        if dict_data.get('thumbnail_url') is None:
            dict_data['thumbnail_url'] = ''

        if dict_data.get('delete_status') is None:
            dict_data['delete_status'] = 'UNDELETED'

        return self._to_category_obj(dict_data)

    def _to_category_obj(self, dict_data):
        data = [
            CategoryID(dict_data["category_id"]),
            AuthorID(dict_data["author_id"]),
            Name(dict_data["name"]),
            Description(dict_data["description"]),
            LastUpdateDate(dict_data["last_update_date"]),
            RegisterDate(dict_data["register_date"]),
            ReleaseStatus[dict_data["release_status"]],
            CategoryType[dict_data["category_type"]],
            ShareRange[dict_data["share_range"]],
            ShareUrl(dict_data["share_url"]),
            ThumbnailUrl(dict_data["thumbnail_url"]),
            DeleteStatus[dict_data["delete_status"]],
        ]
        if CategoryType[dict_data["category_type"]] is CategoryType.COMMON:
            category_obj = CommonCategory(*data)
            return category_obj
        if CategoryType[dict_data["category_type"]] is CategoryType.ALBUM:
            category_obj = AlbumCategory(*data)
            return category_obj
