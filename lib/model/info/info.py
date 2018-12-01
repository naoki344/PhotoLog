from datetime import datetime
from enum import Enum
import copy
'''
Value Object : AuthorID
'''


class AuthorID:
    def __init__(self, author_id):
        self.value = author_id


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

    # 文字数のチェック


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


'''
Value Object : ReleaseStatus
'''


class ReleaseStatus(Enum):
    OPEN = 1
    CLOSE = 2


class Info:
    def __init__(self, author_id: AuthorID, name: Name,
                 description: Description, last_update_date: LastUpdateDate,
                 register_date: RegisterDate, release_status: ReleaseStatus,
                 thumbnail_url: ThumbnailUrl, delete_status: DeleteStatus):

        self.author_id = author_id
        self.name = name
        self.description = description
        self.register_date = register_date
        self.last_update_date = last_update_date
        self.release_status = release_status
        self.thumbnail_url = thumbnail_url
        self.delete_status = delete_status

    def to_dict(self):
        return {
            "author_id": self.author_id.value,
            "name": self.name.value,
            "description": self.description.value,
            "register_date": self.register_date.datetime_string(),
            "last_update_date": self.last_update_date.datetime_string(),
            "release_status": self.release_status.name,
            "thumbnail_url": self.thumbnail_url.value,
            "delete_status": self.delete_status.name,
        }

    @staticmethod
    def from_dict(dict_data: dict) -> 'Info':
        data = (
            AuthorID(dict_data["author_id"]),
            Name(dict_data["name"]),
            Description(dict_data["description"]),
            LastUpdateDate(dict_data["last_update_date"]),
            RegisterDate(dict_data['register_date']),
            ReleaseStatus[dict_data["release_status"]],
            ThumbnailUrl(dict_data["thumbnail_url"]),
            DeleteStatus[dict_data["delete_status"]],
        )
        info_obj = Info(*data)
        return info_obj

    def modify(self, dict_data) -> 'Info':
        now_time = datetime.now()

        new_info = copy.deepcopy(self)

        if dict_data.get('author_id') is not None:
            new_info.author_id = AuthorID(dict_data['author_id'])

        if dict_data.get('name') is not None:
            new_info.name = Name(dict_data['name'])

        if dict_data.get('description') is not None:
            new_info.description = Description(dict_data['description'])

        if dict_data.get('release_status') is not None:
            new_info.release_status = ReleaseStatus[
                dict_data['release_status']]

        if dict_data.get('thumbnail_url') is not None:
            new_info.thumbnail_url = ThumbnailUrl(dict_data['thumbnail_url'])

        if dict_data.get('delete_status') is not None:
            new_info.delete_status = DeleteStatus[dict_data['delete_status']]

        new_info.last_update_date = LastUpdateDate(now_time)

        return new_info
