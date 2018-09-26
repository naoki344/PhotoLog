# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
from lib.model.folder.folder import Folder
from lib.model.folder.folder import FolderID
from lib.model.folder.folder import FolderAuthorID

class FolderRepositories(metaclass=ABCMeta):

    @abstractmethod
    def get_all_folder(self, folder_author_id : FolderAuthorID ):
        pass

    @abstractmethod
    def find_folder(self, folder_id : FolderID ):
        pass

    @abstractmethod
    def register_folder(self, folder : Folder ):
        pass

    @abstractmethod
    def update_folder(self, folder : Folder ):
        pass

    @abstractmethod
    def delete_folder(self, folder_id : FolderID ):
        pass
