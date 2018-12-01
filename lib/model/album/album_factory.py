# -*- coding: utf-8 -*-

import time
import uuid
from datetime import datetime

from lib.model.album.album import Album
from lib.model.album.album import AlbumID
from lib.model.info.info_factory import InfoFactory
from lib.model.share.share_factory import ShareFactory


class AlbumFactory():
    @staticmethod
    def create(dict_data) -> Album:
        now_time = datetime.now()

        if dict_data.get('album_id') is None:
            dict_data['album_id'] = 'album-' + str(uuid.uuid4())

        if dict_data.get('info') is None:
            return False

        if dict_data.get('share') is None:
            return False

        return _to_album_obj(dict_data)


def _to_album_obj(dict_data):
    return Album(
        album_id=AlbumID(dict_data["album_id"]),
        info=InfoFactory.create(dict_data['info']),
        share=ShareFactory.create(dict_data['share']),
    )
