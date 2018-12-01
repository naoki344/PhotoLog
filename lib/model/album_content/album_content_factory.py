# -*- coding: utf-8 -*-

from lib.model.content import Content
from lib.model.album.album import AlbumID
from lib.model.info.info import DeleteStatus
from lib.model.album_content.album_content import AlbumContent


class AlbumContentFactory():
    def create(self, dict_data) -> AlbumContent:

        if dict_data.get('album_id') is None:
            return False

        if dict_data.get('content') is None:
            return False

        if isinstance(dict_data['content'], Content) is False:
            return False

        if dict_data.get('delete_status') is None:
            dict_data['delete_status'] = 'UNDELETED'

        return self._to_album_content_obj(dict_data)

    def _to_album_content_obj(self, dict_data):
        data = [
            dict_data["album_id"],
            dict_data["content"],
            DeleteStatus[dict_data["delete_status"]],
        ]
        album_content_obj = AlbumContent(*data)
        return album_content_obj
