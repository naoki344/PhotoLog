# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

from lib.model.folder.folder import AuthorID, Folder, FolderID


class FolderRepository(metaclass=ABCMeta):
    @abstractmethod
    def find_user_all(self, author_id: AuthorID):
        pass

    @abstractmethod
    def find(self, folder_id: FolderID):
        pass

    @abstractmethod
    def register(self, folder: Folder):
        pass

    @abstractmethod
    def update(self, folder: Folder):
        pass

    @abstractmethod
    def delete(self, folder_id: FolderID):
        pass
