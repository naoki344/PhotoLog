# -*- coding: utf-8 -*-

import datetime
import json
import os
import sys

from app.infrastructure.album import AlbumDataSource
from lib.model.info.info import AuthorID
from lib.model.album.album import Album
from lib.model.album.album import AlbumID
from lib.model.album.album_list import AlbumList
from lib.model.user.user import User


class AlbumQueryService:
    def __init__(self):
        self.album_datasource = AlbumDataSource()

    def find_user_all(self, author_id: AuthorID):
        albums = self.album_datasource.find_user_all(author_id)
        user_album_list = AlbumList(albums)
        return user_album_list

    def find(self, album_id: AlbumID):
        album = self.album_datasource.find(album_id)
        if album is None:
            return None
        return album

    def find_for_gallery(self, album_id: AlbumID, user: User):
        album = self.find(album_id)
        if album is None:
            return None
        if album.can_show_gallery(user):
            return album
        return None


class AlbumCommandService:
    def __init__(self):
        self.album_datasource = AlbumDataSource()

    def register(self, album: Album):
        result = self.album_datasource.register(album)
        return album

    def update(self, org_album: Album, new_album: Album):
        if org_album.can_update():
            updated_album = self.album_datasource.update(new_album)
        return updated_album

    def delete(self, album: Album):
        if album.can_delete():
            deleted_album = self.album_datasource.delete(album)
        return deleted_album
