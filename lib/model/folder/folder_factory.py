# -*- coding: utf-8 -*-

import time
import uuid
from datetime import datetime

from lib.model.folder.folder import (Folder, FolderAuthorID, FolderDeleteFlag,
                                     FolderDescription, FolderID,
                                     FolderLastUpdateDate, FolderName,
                                     FolderRegisterDate, FolderReleaseStatus,
                                     FolderShareRange, FolderShareUrl,
                                     FolderThumbnailUrl)


class FolderFactory():
    def create(self, dict_data) -> Folder:
        delete_flag = 0
        now_time = datetime.now()

        if dict_data.get('folder_id') == None:
            dict_data['folder_id'] = 'folder-' + str(uuid.uuid4())

        if dict_data.get('author_id') == None:
            return False

        if dict_data.get('name') == None:
            return False

        if dict_data.get('description') == None:
            dict_data['description'] = ''

        if dict_data.get('register_date') == None:
            dict_data['register_date'] = now_time

        if dict_data.get('last_update_date') == None:
            dict_data['last_update_date'] = now_time

        if dict_data.get('release_status') == None:
            dict_data['release_status'] = 'OPEN'

        if dict_data.get('share_range') == None:
            dict_data['share_range'] = 'PRIVATE'

        if dict_data.get('share_url') == None:
            dict_data['share_url'] = ''

        if dict_data.get('thumbnail_url') == None:
            dict_data['thumbnail_url'] = ''

        if dict_data.get('delete_status') == None:
            dict_data['delete_status'] = 'UNDELETED'

        return self._to_folder_obj(dict_data)

    def _to_folder_obj(self, dict_data):
        data = [
            FolderID(dict_data["folder_id"]),
            FolderAuthorID(dict_data["author_id"]),
            FolderName(dict_data["name"]),
            FolderDescription(dict_data["description"]),
            FolderLastUpdateDate(dict_data["last_update_date"]),
            FolderRegisterDate(dict_data["register_date"]),
            FolderReleaseStatus[dict_data["release_status"]],
            FolderShareRange[dict_data["share_range"]],
            FolderShareUrl(dict_data["share_url"]),
            FolderThumbnailUrl(dict_data["thumbnail_url"]),
            FolderDeleteFlag[dict_data["delete_status"]],
        ]
        folder_obj = Folder(*data)
        return folder_obj
