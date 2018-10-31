# -*- coding: utf-8 -*-
from enum import Enum
import datetime
from lib.model.category.category import Category


class CategoryList():
    def __init__(self, category_obj_list):
        self.category_list = category_obj_list

    def add_category(self, category: Category):
        self.category_list.append(category)

    def to_dict(self):
        category_dict_list = []
        for category_obj in self.category_list:
            category_dict_list.append(category_obj.to_dict())

        return category_dict_list
