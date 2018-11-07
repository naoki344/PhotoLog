import time
import uuid
from datetime import datetime

from lib.model.info.info import Info
from lib.model.info.info import AuthorID
from lib.model.info.info import DeleteStatus
from lib.model.info.info import Description
from lib.model.info.info import LastUpdateDate
from lib.model.info.info import Name
from lib.model.info.info import RegisterDate
from lib.model.info.info import ReleaseStatus
from lib.model.info.info import ThumbnailUrl


class InfoFactory:
    @staticmethod
    def create(dict_data) -> Info:
        now_time = datetime.now()

        if dict_data.get('author_id') is None:
            return False

        if dict_data.get('name') is None:
            return False

        if dict_data.get('description') is None:
            dict_data['description'] = ''

        if dict_data.get('register_date') is None:
            dict_data['register_date'] = now_time

        if dict_data.get('last_update_date') is None:
            dict_data['last_update_date'] = now_time

        if dict_data.get('release_status') is None:
            dict_data['release_status'] = 'OPEN'

        if dict_data.get('thumbnail_url') is None:
            dict_data['thumbnail_url'] = ''

        if dict_data.get('delete_status') is None:
            dict_data['delete_status'] = 'UNDELETED'

        return _to_info_obj(dict_data)


def _to_info_obj(dict_data):
    data = [
        AuthorID(dict_data["author_id"]),
        Name(dict_data["name"]),
        Description(dict_data["description"]),
        LastUpdateDate(dict_data["last_update_date"]),
        RegisterDate(dict_data["register_date"]),
        ReleaseStatus[dict_data["release_status"]],
        ThumbnailUrl(dict_data["thumbnail_url"]),
        DeleteStatus[dict_data["delete_status"]],
    ]
    info_obj = Info(*data)
    return info_obj
