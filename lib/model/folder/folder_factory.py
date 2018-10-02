# -*- coding: utf-8 -*-

import uuid
import time
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
    def create(self, dict_data) -> Folder:
        folder_uuid = 'folder-' + str(uuid.uuid4())
        delete_flag = 0
        now_time = datetime.now()

        data = [
            FolderID(folder_uuid),
            FolderAuthorID(dict_data["author_id"]),
            FolderName(dict_data["name"]),
            FolderDescription(dict_data["description"]),
            FolderLastUpdateDate(now_time),
            FolderRegisterDate(now_time),
            FolderReleaseStatus(dict_data["release_status"]),
            FolderShareRange(dict_data["share_range"]),
            FolderShareUrl(dict_data["share_url"]),
            FolderThumbnailUrl(dict_data["thumbnail_url"]),
            FolderDeleteFlag(delete_flag),
        ]
        folder_obj = Folder(*data)
        return folder_obj

    def restore(self, dict_data) -> Folder:
        now_time = datetime.now()
        data = [
            FolderID(dict_data["folder_id"]),
            FolderAuthorID(dict_data["author_id"]),
            FolderName(dict_data["name"]),
            FolderDescription(dict_data["description"]),
            FolderLastUpdateDate(now_time),
            FolderRegisterDate(now_time),
            FolderReleaseStatus(dict_data["release_status"]),
            FolderShareRange(dict_data["share_range"]),
            FolderShareUrl(dict_data["share_url"]),
            FolderThumbnailUrl(dict_data["thumbnail_url"]),
            FolderDeleteFlag(dict_data["delete_flag"]),
        ]
        folder_obj = Folder(*data)
        return folder_obj
