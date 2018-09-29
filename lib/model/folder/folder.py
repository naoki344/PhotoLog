# -*- coding: utf-8 -*-
from datetime import datetime
from enum import Enum


'''
Value Object : ID
'''


class FolderID:
    def __init__(self, folder_id):
        self.value = folder_id

    def __check_exist_user(self):
        return True


'''
Value Object : AuthorID
'''


class FolderAuthorID:
    def __init__(self, user_id):
        self.value = user_id

    def __check_exist_user(self):
        return True


'''
Value Object : Name
'''


class FolderName:
    def __init__(self, name):
        self.value = name


'''
Value Object : Description
'''


class FolderDescription:
    def __init__(self, description_txt):
        self.value = description_txt

    def __check_character_limit(self):
        return True

    #文字数のチェック


'''
Value Object : LastUpdateDate
'''


class FolderLastUpdateDate:
    def __init__(self, date):
        self.value = date

    def datetime_string():
        return datetime.fromtimestamp(self.value).isoformat()


'''
Value Object : RegisterDate
'''


class FolderRegisterDate:
    def __init__(self, date):
        self.value = date

    def datetime_string():
        return datetime.fromtimestamp(self.value).isoformat()


'''
Value Object : ReleaseStatus
'''


class FolderReleaseStatus(Enum):
    NONE = 0
    OPEN = 1
    CLOSE = 2


'''
Value Object : ShareRange
'''


class FolderShareRange(Enum):
    NONE = 0
    PRIVATE = 1
    PUBLIC = 2
    PASSFRASE = 3


'''
Value Object : ShareUrl
'''


class FolderShareUrl:
    def __init__(self, share_url):
        self.value = share_url


'''
Value Object : ThumbnailUrl
'''


class FolderThumbnailUrl:
    def __init__(self, thumbnail_url):
        self.value = thumbnail_url


'''
Value Object : DeleteFlag
'''


class FolderDeleteFlag(Enum):
    NONE = 0
    DELETED = 1


class Folder():
    def __init__(self, folder_id: FolderID, author_id: FolderAuthorID,
                 name: FolderName, description: FolderDescription,
                 last_update_date: FolderLastUpdateDate,
                 register_date: FolderRegisterDate,
                 release_status: FolderReleaseStatus,
                 share_range: FolderShareRange, share_url: FolderShareUrl,
                 thumbnail_url: FolderThumbnailUrl,
                 delete_flag: FolderDeleteFlag):

        self.folder_id = folder_id
        self.author_id = author_id
        self.name = name
        self.description = description
        self.register_date = register_date
        self.last_update_date = last_update_date
        self.release_status = release_status
        self.share_range = share_range
        self.share_url = share_url
        self.thumbnail_url = thumbnail_url
        self.delete_flag = delete_flag

    def to_dict(self):
        return {
            "folder_id": self.folder_id.value,
            "author_id": self.author_id.value,
            "name": self.name.value,
            "description": self.description.value,
            "register_date": self.register_date.value.isoformat(),
            "last_update_date": self.last_update_date.datetime_string(),
            "release_status": self.release_status.datetime_string(),
            "share_range": self.share_range.value,
            "share_url": self.share_url.value,
            "thumbnail_url": self.thumbnail_url.value,
            "delete_flag": self.delete_flag.value,
        }
