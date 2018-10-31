# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

from lib.model.category.category import AuthorID, Category, CategoryID


class CategoryRepository(metaclass=ABCMeta):
    @abstractmethod
    def find_user_all(self, author_id: AuthorID):
        pass

    @abstractmethod
    def find(self, category_id: CategoryID):
        pass

    @abstractmethod
    def register(self, category: Category):
        pass

    @abstractmethod
    def update(self, category: Category):
        pass

    @abstractmethod
    def delete(self, category_id: CategoryID):
        pass
