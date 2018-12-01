# -*- coding: utf-8 -*-

import datetime
import json
import os
import sys

from lib.model.info.info import AuthorID
from app.infrastructure.category import CategoryDataSource
from lib.model.category.category import CommonCategory
from lib.model.category.category import CategoryID
from lib.model.category.category import CategoryType
from lib.model.category.category_list import CategoryList


class CommonCategoryQueryService:
    def __init__(self):
        self.common_category_datasource = CategoryDataSource()

    def find_user_all(self, author_id: AuthorID):
        common_categorys = self.common_category_datasource.find_user_all(
            author_id, CategoryType['COMMON_CATEGORY'])
        user_common_category_list = CategoryList(common_categorys)
        return user_common_category_list

    def find(self, common_category_id: CategoryID):
        common_category = self.common_category_datasource.find(
            common_category_id)
        if common_category == None:
            return None
        return common_category


class CommonCategoryCommandService:
    def __init__(self):
        self.common_category_datasource = CategoryDataSource()

    def register(self, common_category: CommonCategory):
        result = self.common_category_datasource.register(common_category)
        return common_category

    def update(self, org_common_category: CommonCategory,
               new_common_category: CommonCategory):
        if org_common_category.can_update():
            updated_common_category = self.common_category_datasource.update(
                new_common_category)
        return updated_common_category

    def delete(self, common_category: CommonCategory):
        if common_category.can_delete():
            deleted_common_category = self.common_category_datasource.delete(
                common_category)
        return deleted_common_category
