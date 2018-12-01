# -*- coding: utf-8 -*-
import copy
from enum import Enum

from lib.model.info.info import DeleteStatus
from lib.model.content import ContentID
from lib.model.content import Content
from lib.model.album.album import AlbumID


class AlbumContent:
    def __init__(self, album_id: AlbumID, content: Content,
                 delete_status: DeleteStatus):

        self.album_id = album_id
        self.content = content
        self.delete_status = delete_status

    def to_dict(self):
        content = self.content.to_dict()
        content['content_id'] = self.content.content_id.value
        return {
            "album_id": self.album_id.value,
            "content_type": self.content.get_content_type(),
            "delete_status": self.delete_status.name,
            "content": content,
        }

    def can_delete(self):
        return True

    @staticmethod
    def from_dict(dict_data: dict) -> 'AlbumContent':
        data = (
            dict_data["album_id"],
            dict_data['content_obj'],
            dict_data['delete_status'],
        )
        return AlbumContent(*data)
