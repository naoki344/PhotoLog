# -*- coding: utf-8 -*-
import copy
from enum import Enum

from lib.model.info.info import DeleteStatus
from lib.model.content import ContentID
from lib.model.content import Content
from lib.model.content import ContentList
from lib.model.album.album import AlbumID


class AlbumContentList:
    def __init__(self, album_id: AlbumID, content_list: ContentList):

        self.album_id = album_id
        self.content_list = content_list

    def to_dict(self):
        return {
            "album_id": self.album_id.value,
            "content_list": self.content_list.to_dict(),
        }

    def can_delete(self):
        return True

    @staticmethod
    def from_dict(dict_data: dict) -> 'AlbumContentList':
        data = (
            dict_data["album_id"],
            ContentList(dict_data['content_obj_list']),
        )
        return AlbumContentList(*data)
