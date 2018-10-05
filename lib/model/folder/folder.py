# -*- coding: utf-8 -*-
import copy
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


class AuthorID:
    def __init__(self, user_id):
        self.value = user_id


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
Value Object : DeleteFlag
'''


class DeleteStatus(Enum):
    UNDELETED = 0
    DELETED = 1


class Folder:
    def __init__(self, folder_id: FolderID, author_id: AuthorID, name: Name,
                 description: Description, last_update_date: LastUpdateDate,
                 register_date: RegisterDate, release_status: ReleaseStatus,
                 share_range: ShareRange, share_url: ShareUrl,
                 thumbnail_url: ThumbnailUrl, delete_status: DeleteStatus):

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
        self.delete_status = delete_status

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
            "delete_status": self.delete_status.name,
        }

    def can_delete(self):
        return True

    def can_update(self):
        return True

    @staticmethod
    def from_dict(dict_data: dict) -> 'Folder':
        data = [
            FolderID(dict_data["folder_id"]),
            AuthorID(dict_data["author_id"]),
            Name(dict_data["name"]),
            Description(dict_data["description"]),
            LastUpdateDate(dict_data["last_update_date"]),
            RegisterDate(dict_data['register_date']),
            ReleaseStatus[dict_data["release_status"]],
            ShareRange[dict_data["share_range"]],
            ShareUrl(dict_data["share_url"]),
            ThumbnailUrl(dict_data["thumbnail_url"]),
            DeleteStatus[dict_data["delete_status"]],
        ]
        folder_obj = Folder(*data)
        return folder_obj

    def modify(self, dict_data) -> 'Folder':
        now_time = datetime.now()

        new_folder = copy.deepcopy(self)

        if dict_data.get('author_id') is not None:
            new_folder.author_id = AuthorID(dict_data['author_id'])

        if dict_data.get('name') is not None:
            new_folder.name = Name(dict_data['name'])

        if dict_data.get('description') is not None:
            new_folder.description = Description(dict_data['description'])

        if dict_data.get('release_status') is not None:
            new_folder.release_status = ReleaseStatus[
                dict_data['release_status']]

        if dict_data.get('share_range') is not None:
            new_folder.share_range = ShareRange[dict_data['share_range']]

        if dict_data.get('share_url') is not None:
            new_folder.share_url = ShareUrl(dict_data['share_url'])

        if dict_data.get('thumbnail_url') is not None:
            new_folder.thumbnail_url = ThumbnailUrl(dict_data['thumbnail_url'])

        if dict_data.get('delete_status') is not None:
            new_folder.delete_status = DeleteFlag[dict_data['delete_status']]

        new_folder.last_update_date = LastUpdateDate(now_time)

        return new_folder
