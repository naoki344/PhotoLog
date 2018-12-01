# -*- coding: utf-8 -*-

from lib.model.info.info import AuthorID
from lib.model.info.info import DeleteStatus
from lib.model.album.album import Album
from lib.model.album.album import AlbumID

from .datasource import DataSource


class AlbumDataSource():
    def __init__(self):
        self.datasource = DataSource()
        self.db_prefix = self.datasource.get_prefix()

    def find_user_all(self, author_id: AuthorID):
        sql = 'SELECT * FROM {}_album WHERE author_id=%s AND delete_status="UNDELETED";'.format(
            self.db_prefix)
        parameter = [author_id.value]
        albums = self.datasource.get(sql, parameter, True)
        album_obj_list = []
        for album_row in albums:
            album_obj = self._to_album_obj(album_row)
            album_obj_list.append(album_obj)

        return album_obj_list

    def find(self, album_id: AlbumID):
        sql = 'SELECT * FROM {}_album WHERE album_id=%s;'.format(
            self.db_prefix)
        parameter = [album_id.value]
        albums = self.datasource.get(sql, parameter, True)
        if len(albums) == 0:
            return None

        album_row = albums[0]
        album_obj = self._to_album_obj(album_row)
        return album_obj

    def register(self, album: Album):
        sql = 'INSERT INTO {}_album(album_id,author_id,name,description,register_date,last_update_date,release_status,thumbnail_url,delete_status,share_range,share_password) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ;'.format(
            self.db_prefix)
        parameter = [
            album.album_id.value,
            album.info.author_id.value,
            album.info.name.value,
            album.info.description.value,
            album.info.register_date.value,
            album.info.last_update_date.value,
            album.info.release_status.name,
            album.info.thumbnail_url.value,
            album.info.delete_status.name,
            album.share.share_range.name,
            album.share.share_password.value,
        ]
        album_id = self.datasource.insert(sql, parameter, True)

        return True

    def update(self, album: Album):
        sql = 'UPDATE {}_album SET author_id=%s,name=%s,description=%s,register_date=%s,last_update_date=%s,release_status=%s,share_range=%s,share_url=%s,thumbnail_url=%s,delete_status=%s WHERE album_id=%s;'.format(
            self.db_prefix)
        parameter = [
            album.info.author_id.value, album.info.name.value,
            album.info.description.value, album.info.register_date.value,
            album.info.last_update_date.value, album.info.release_status.name,
            album.info.thumbnail_url.value, album.share.share_range.name,
            album.share.share_url.value, album.info.delete_status.name,
            album.album_id.value
        ]
        self.datasource.update(sql, parameter, True)
        album_id = album.album_id

        return self.find(album_id)

    def delete(self, album: Album):
        album_id = album.album_id.value
        sql = 'UPDATE {}_album SET delete_status="DELETED" WHERE album_id=%s;'.format(
            self.db_prefix)
        parameter = [album_id]
        try:
            ret_status = self.datasource.update(sql, parameter, True)
        except:
            raise

        return True

    def _to_album_obj(self, album_row):
        album_obj = Album.from_dict(album_row)
        return album_obj
