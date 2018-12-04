# -*- coding: utf-8 -*-
import copy
from datetime import datetime
from enum import Enum

from lib.model.content import Content
from lib.model.content import ContentID
from lib.model.info.info import Info
from lib.model.share.share import Share
'''
Value Object : ID
'''


class FolderID(ContentID):
    def __init__(self, folder_id: str):
        self.value = folder_id


class Folder(Content):
    def __init__(self, folder_id: FolderID, info: Info, share: Share):

        self.folder_id = folder_id
        self.info = info
        self.share = share
        self.content_id = folder_id

    def to_dict(self):
        return {
            'folder_id': self.folder_id.value,
            'info': self.info.to_dict(),
            'share': self.share.to_dict(),
        }

    def can_delete(self):
        return True

    def can_update(self):
        return True

    @staticmethod
    def from_dict(dict_data: dict) -> 'Folder':
        return Folder(
            folder_id=FolderID(dict_data["folder_id"]),
            info=Info.from_dict(dict_data),
            share=Share.from_dict(dict_data),
        )

    def modify(self, dict_data) -> 'Folder':
        new_folder = copy.deepcopy(self)

        if dict_data.get('info') is not None:
            new_folder.info = self.info.modify(dict_data['info'])

        if dict_data.get('share') is not None:
            new_folder.share = self.share.modify(dict_data['share'])

        return new_folder

    def get_content_id(self):
        return self.folder_id

    def get_content_type(self):
        return 'Folder'
