# -*- coding: utf-8 -*-
import copy
from datetime import datetime
from enum import Enum
'''
Value Object : ID
'''


class AlbumID:
    def __init__(self, album_id):
        self.value = album_id


'''
Value Object : AuthorID
'''


class AuthorID:
    def __init__(self, user_id):
        self.value = user_id


'''
Value Object : ContentID
'''


class ContentID:
    def __init__(self, content_id):
        self.value = content_id


'''
Value Object : Name
'''


class Name:
    def __init__(self, name):
        self.value = name


'''
Value Object : Description
'''


class Description:
    def __init__(self, description_txt):
        self.value = description_txt

    def __check_character_limit(self):
        return True

    #文字数のチェック


'''
Value Object : LastUpdateDate
'''


class LastUpdateDate:
    def __init__(self, date=None):
        self.value = date

    def datetime_string(self):
        return self.value.isoformat()


'''
Value Object : RegisterDate
'''


class RegisterDate:
    def __init__(self, date=None):
        self.value = date

    def datetime_string(self):
        return self.value.isoformat()


'''
Value Object : ReleaseStatus
'''


class ReleaseStatus(Enum):
    OPEN = 1
    CLOSE = 2


'''
Value Object : ShareRange
'''


class ShareRange(Enum):
    PRIVATE = 1
    PUBLIC = 2
    PASSFRASE = 3


'''
Value Object : ShareUrl
'''


class ShareUrl:
    def __init__(self, share_url):
        self.value = share_url


'''
Value Object : ThumbnailUrl
'''


class ThumbnailUrl:
    def __init__(self, thumbnail_url):
        self.value = thumbnail_url


'''
Value Object : DeleteStatus
'''


class DeleteStatus(Enum):
    UNDELETED = 0
    DELETED = 1


class Content:
    def __init__(self, album_id: AlbumID, content_id: ContentID,
                 delete_status: DeleteStatus):

        self.album_id = album_id
        self.content_id = ContentID
        self.delete_status = delete_status

    def to_dict(self):
        return {
            "album_id": self.album_id.value,
            "content_id": self.content_id.value,
            "delete_status": self.delete_status.name,
        }

    def can_delete(self):
        return True

    def can_update(self):
        return True

    @staticmethod
    def from_dict(dict_data: dict) -> 'Content':
        data = [
            AlbumID(dict_data["album_id"]),
            ContentID(dict_data["content_id"]),
            DeleteStatus[dict_data["delete_status"]],
        ]
        content_obj = Content(*data)
        return content_obj

    def modify(self, dict_data) -> 'Content':

        new_content = copy.deepcopy(self)

        if dict_data.get('delete_status') is not None:
            new_content.delete_status = DeleteStatus[
                dict_data['delete_status']]

        return new_content
