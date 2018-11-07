# -*- coding: utf-8 -*-

from lib.model.album.album import AlbumID
from lib.model.album_content.album_content_list import AlbumContentList
from lib.model.album_content.album_content import AlbumContent
from lib.model.category.category import Category
from lib.model.info.info import AuthorID
from lib.model.info.info import DeleteStatus
from lib.model.content import Content
from lib.model.content import ContentID

from .datasource import DataSource
from app.infrastructure.folder import FolderDataSource
from app.infrastructure.category import CategoryDataSource


class AlbumContentDataSource:
    def __init__(self):
        self.datasource = DataSource()
        self.folder_datasource = FolderDataSource()
        self.category_datasource = CategoryDataSource()
        self.db_prefix = self.datasource.get_prefix()

    def find_by_album_id(self, album_id: AlbumID):
        sql = 'SELECT * FROM {}_album_content WHERE album_id=%s AND delete_status=%s;'.format(
            self.db_prefix)
        parameter = [album_id.value, DeleteStatus.UNDELETED.name]
        album_content_rel_list = self.datasource.get(sql, parameter, True)
        if len(album_content_rel_list) == 0:
            return None
        content_obj_list = []
        for album_content_rel in album_content_rel_list:
            content_id = ContentID(album_content_rel['content_id'])
            content_obj_list.append(self._to_album_content_obj(content_id))

        data = {'album_id': album_id, 'content_obj_list': content_obj_list}
        return AlbumContentList.from_dict(data)

    def find(self, album_id: AlbumID, content_id: ContentID):
        sql = 'SELECT * FROM {}_album_content WHERE album_id=%s AND content_id=%s;'.format(
            self.db_prefix)
        parameter = [album_id.value, content_id.value]
        album_content_rel_list = self.datasource.get(sql, parameter, True)
        if len(album_content_rel_list) == 0:
            return None
        album_content_rel = album_content_rel_list[0]
        content_id = ContentID(album_content_rel['content_id'])
        content_obj = self._to_album_content_obj(content_id)
        delete_status = DeleteStatus[album_content_rel['delete_status']]

        data = {
            'album_id': album_id,
            'content_obj': content_obj,
            'delete_status': delete_status
        }
        return AlbumContent.from_dict(data)

    def register(self, album_id: AlbumID, content_id: ContentID):
        sql = 'INSERT INTO {}_album_content(album_id,content_id,delete_status) VALUES(%s,%s,%s) ;'.format(
            self.db_prefix)
        parameter = [
            album_id.value, content_id.value, DeleteStatus.UNDELETED.name
        ]
        self.datasource.insert(sql, parameter, True)

        return True

    def delete(self, album_id: AlbumID, content_id: ContentID):
        try:
            sql = 'UPDATE {}_album_content SET delete_status=%s WHERE album_id=%s AND content_id=%s;'.format(
                self.db_prefix)
            parameter = [
                DeleteStatus.DELETED.name,
                album_id.value,
                content_id.value,
            ]
            self.datasource.update(sql, parameter, True)

        except:
            raise

        return True

    # モデルに置き換える
    def _to_album_content_obj(self, content_id: ContentID):
        content_type = Content.check_content_type(content_id)
        if content_type == 'folder':
            return self.folder_datasource.find(content_id)
        if content_type == 'album_category' or content_type(
        ) == 'common_category':
            return self.category_datasource.find(content_id)
