# -*- coding: utf-8 -*-

import uuid
from datetime import datetime

from lib.model.folder.folder import Folder
from lib.model.folder.folder import FolderAuthorID
from lib.model.folder.folder import FolderDeleteFlag
from lib.model.folder.folder import FolderDescription
from lib.model.folder.folder import FolderID
from lib.model.folder.folder import FolderLastUpdateDate
from lib.model.folder.folder import FolderName
from lib.model.folder.folder import FolderRegisterDate
from lib.model.folder.folder import FolderReleaseStatus
from lib.model.folder.folder import FolderShareRange
from lib.model.folder.folder import FolderShareUrl
from lib.model.folder.folder import FolderThumbnailUrl


class FolderFactory():
    def create(self, recive_data) -> Folder:
        folder_uuid = 'folder' + ruuid.uuid4()
        delete_flag = 0
        now_time = int(time.mktime(now.timetuple()))

        data = [
            FolderID(folder_uuid),
            FolderAuthorID(recive_data["author_id"]),
            FolderName(recive_data["name"]),
            FolderDescription(recive_data["description"]),
            FolderLastUpdateDate(now_time),
            FolderRegisterDate(now_time),
            FolderReleaseStatus(recive_data["release_status"]),
            FolderShareRange(recive_data["share_range"]),
            FolderShareUrl(recive_data["share_url"]),
            FolderThumbnailUrl(recive_data["thumbnail_url"]),
            FolderDeleteFlag(delete_flag),
        ]
        folder_obj = Folder(*data)
        return folder_obj

    def restore(self, data) -> Folder:
        data = [
            FolderID(recive_data["folder_id"]),
            FolderAuthorID(recive_data["author_id"]),
            FolderName(recive_data["name"]),
            FolderDescription(recive_data["description"]),
            FolderLastUpdateDate(now_time),
            FolderRegisterDate(now_time),
            FolderReleaseStatus(recive_data["release_status"]),
            FolderShareRange(recive_data["share_range"]),
            FolderShareUrl(recive_data["share_url"]),
            FolderThumbnailUrl(recive_data["thumbnail_url"]),
            FolderDeleteFlag(recive_data["delete_flag"]),
        ]
        folder_obj = Folder(*data)
        return folder_obj
