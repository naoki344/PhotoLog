# -*- coding: utf-8 -*-
import copy
from datetime import datetime
from enum import Enum

from lib.model.info.info import Info
from lib.model.share.share import Share
'''
Value Object : ID
'''


class AlbumID:
    def __init__(self, album_id: str):
        self.value = album_id


class Album:
    def __init__(self, album_id: AlbumID, info: Info, share: Share):

        self.album_id = album_id
        self.info = info
        self.share = share

    def to_dict(self):
        return {
            'album_id': self.album_id.value,
            'info': self.info.to_dict(),
            'share': self.share.to_dict(),
        }

    def can_delete(self):
        return True

    def can_update(self):
        return True

    @staticmethod
    def from_dict(dict_data: dict) -> 'Album':
        return Album(
            album_id=AlbumID(dict_data["album_id"]),
            info=Info.from_dict(dict_data),
            share=Share.from_dict(dict_data),
        )

    def modify(self, dict_data) -> 'Album':
        new_album = copy.deepcopy(self)

        if dict_data.get('info') is not None:
            new_album.info = self.info.modify(dict_data['info'])

        if dict_data.get('share') is not None:
            new_album.info = self.share.modify(dict_data['share'])

        return new_album
