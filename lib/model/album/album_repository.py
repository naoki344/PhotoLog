# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

from lib.model.album.album import AuthorID, Album, AlbumID


class AlbumRepository(metaclass=ABCMeta):
    @abstractmethod
    def find_user_all(self, author_id: AuthorID):
        pass

    @abstractmethod
    def find(self, album_id: AlbumID):
        pass

    @abstractmethod
    def register(self, album: Album):
        pass

    @abstractmethod
    def update(self, album: Album):
        pass

    @abstractmethod
    def delete(self, album_id: AlbumID):
        pass
