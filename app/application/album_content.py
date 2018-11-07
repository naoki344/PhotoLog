from app.infrastructure.album_content import AlbumContentDataSource
from lib.model.content import Content
from lib.model.content import ContentID
from lib.model.album_content.album_content_list import AlbumContentList
from lib.model.album_content.album_content import AlbumContent
from lib.model.info.info import AuthorID
from lib.model.album.album import AlbumID
from lib.model.album.album import Album


class AlbumContentQueryService:
    def __init__(self):
        self.album_content_datasource = AlbumContentDataSource()

    def find_by_album_id(self, album_id: AlbumID):
        return self.album_content_datasource.find_by_album_id(album_id)

    def find(self, album_id: AlbumID, content_id: ContentID):
        album_content = self.album_content_datasource.find(
            album_id, content_id)
        if album_content is None:
            return None
        return album_content


class AlbumContentCommandService:
    def __init__(self):
        self.album_content_datasource = AlbumContentDataSource()

    def register(self, album_content: AlbumContent):
        self.album_content_datasource.register(
            album_content.album_id, album_content.content.get_content_id())

    def delete(self, album_content: AlbumContent):
        self.album_content_datasource.delete(
            album_content.album_id, album_content.content.get_content_id())
