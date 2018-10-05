# -*- coding: utf-8 -*-
from datetime import datetime
from enum import Enum


'''
Value Object : ID
'''


class FolderID:
    def __init__(self, folder_id):
        self.value = folder_id


'''
Value Object : AuthorID
'''


class FolderAuthorID:
    def __init__(self, user_id):
        self.value = user_id


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
    def __init__(self, date=None):
        self.value = date

    def datetime_string(self):
        return self.value.isoformat()


'''
Value Object : RegisterDate
'''


class FolderRegisterDate:
    def __init__(self, date=None):
        self.value = date

    def datetime_string(self):
        return self.value.isoformat()


'''
Value Object : ReleaseStatus
'''


class FolderReleaseStatus(Enum):
    OPEN = 1
    CLOSE = 2


'''
Value Object : ShareRange
'''


class FolderShareRange(Enum):
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
    UNDELETED = 0
    DELETED = 1


class Folder:
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
            "register_date": self.register_date.datetime_string(),
            "last_update_date": self.last_update_date.datetime_string(),
            "release_status": self.release_status.name,
            "share_range": self.share_range.name,
            "share_url": self.share_url.value,
            "thumbnail_url": self.thumbnail_url.value,
            "delete_status": self.delete_flag.name,
        }

    def can_delete(self):
        return True

    def can_update(self):
        return True

    @staticmethod
    def from_dict(dict_data: dict) -> 'Folder':
        data = [
            FolderID(dict_data["folder_id"]),
            FolderAuthorID(dict_data["author_id"]),
            FolderName(dict_data["name"]),
            FolderDescription(dict_data["description"]),
            FolderLastUpdateDate(dict_data["last_update_date"]),
            FolderRegisterDate(dict_data['register_date']),
            FolderReleaseStatus[dict_data["release_status"]],
            FolderShareRange[dict_data["share_range"]],
            FolderShareUrl(dict_data["share_url"]),
            FolderThumbnailUrl(dict_data["thumbnail_url"]),
            FolderDeleteFlag[dict_data["delete_status"]],
        ]
        folder_obj = Folder(*data)
        return folder_obj
