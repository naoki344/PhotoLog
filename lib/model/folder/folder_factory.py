# -*- coding: utf-8 -*-

import time
import uuid
from datetime import datetime

from lib.model.folder.folder import Folder
from lib.model.folder.folder import FolderID
from lib.model.info.info_factory import InfoFactory
from lib.model.share.share_factory import ShareFactory


class FolderFactory():
    @staticmethod
    def create(dict_data) -> Folder:
        now_time = datetime.now()

        if dict_data.get('folder_id') is None:
            dict_data['folder_id'] = 'folder-' + str(uuid.uuid4())

        if dict_data.get('info') is None:
            return False

        if dict_data.get('share') is None:
            return False

        return _to_folder_obj(dict_data)


def _to_folder_obj(dict_data):
    return Folder(
        folder_id=FolderID(dict_data["folder_id"]),
        info=InfoFactory.create(dict_data['info']),
        share=ShareFactory.create(dict_data['share']),
    )
