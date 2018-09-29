# -*- coding: utf-8 -*-

from abc import ABCMeta
from abc import abstractmethod

from lib.model.folder.folder import Folder
from lib.model.folder.folder import FolderAuthorID
from lib.model.folder.folder import FolderID


class FolderRepository(metaclass=ABCMeta):

    @abstractmethod
    def find_user_all(self, folder_author_id : FolderAuthorID ):
        pass

    @abstractmethod
    def find(self, folder_id : FolderID ):
        pass

    @abstractmethod
    def register(self, folder : Folder ):
        pass

    @abstractmethod
    def update(self, folder : Folder ):
        pass

    @abstractmethod
    def delete(self, folder_id : FolderID ):
        pass
