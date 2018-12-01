# -*- coding: utf-8 -*-
from enum import Enum
import datetime
from lib.model.album.album import Album


class AlbumList():
    def __init__(self, album_obj_list):
        self.album_list = album_obj_list

    def add_album(self, album: Album):
        self.album_list.append(album)

    def to_dict(self):
        album_dict_list = []
        for album_obj in self.album_list:
            album_dict_list.append(album_obj.to_dict())

        return album_dict_list
