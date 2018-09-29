# -*- coding: utf-8 -*-

import uuid
from datetime import datetime

from lib.model.folder.folder import (Folder, FolderAuthorID, FolderDeleteFlag,
                                     FolderDescription, FolderID,
                                     FolderLastUpdateDate, FolderName,
                                     FolderRegisterDate, FolderReleaseStatus,
                                     FolderShareRange, FolderShareUrl,
                                     FolderThumbnailUrl)


class FolderFactory():
    def create_folder(self, recive_data) -> Folder:
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

    def restore_folder(self, data) -> Folder:
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
