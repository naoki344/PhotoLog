# -*- coding: utf-8 -*-

from lib.model.album.album import AlbumID
from lib.model.content.content import AlbumContent
from lib.model.content.content import Content
from lib.model.category.category import Category
from lib.model.content.content import AuthorID
from lib.model.content.content import ContentID

from .datasource import DataSource


class AlbumContentDataSource:
    def __init__(self):
        self.datasource = DataSource()
        self.db_prefix = self.datasource.get_prefix()


#
#    def find_all(self, author_id: AuthorID):
#        pass
#
#    def find(self, content: Content):
#        pass
#
#    def find_by_content_id(self, content_id: ContentID):
#        pass
#
#    def find_by_album_id(self, content_id: ContentID):
#        pass

    def register(self, album_id: AlbumID, content: Content):
        sql = 'INSERT INTO {}_album_content(album_id,content_id,content_type,delete_status) VALUES(%s,%s,%s,%s) ;'.format(
            self.db_prefix)
        parameter = [
            album_id.value, content.content_id, content.content_type.name,
            content.delete_status.name
        ]
        self.datasource.insert(sql, parameter, True)

        return True

    def delete(self, album_id: AlbumID, content: Content):
        sql = 'UPDATE {}_album_content SET delete_status="DELETED" WHERE album_id=%s AND content_id=%s;'.format(
            self.db_prefix)
        parameter = [album_id.value, content.content_id.value]
        try:
            self.datasource.update(sql, parameter, True)
        except:
            raise

        return True

    def _to_album_content_obj(self, content_row):
        content_obj = AlbumContent.from_dict(content_row)
        return content_obj
