#/usr/bin/python3

import os
import datetime
from ShareValueObject import *
from test_mod import *


class Folder():

  def __init__( self, author_id, name, description, last_update_date, register_date,release_status, share_range, share_url, thumbnail_url ):
    self.author = AuthorID( author_id )
    self.description = Description( description )
    self.name = Name( name )
    self.last_update_date = LastUpdateDate( last_update_date )
    self.register_date = RegisterDate( register_date )
    self.release_status = ReleaseStatus( release_status )
    self.share_range = ShareRange( share_range )
    self.share_url = ShareUrl( share_url )
    self.thumbnail_url = ThumbnailUrl( thumbnail_url )

# インスタンスの作成
folder_obj = Folder(1,'taro', '太郎のフォルダです', datetime.datetime.today(), datetime.datetime.today(), 1, 2,'https://share.url', 'https://thumbnail.url')
print ( folder_obj.author.value )
print ( folder_obj.name.value )
print ( folder_obj.description.value )
print ( folder_obj.last_update_date.value )
print ( folder_obj.register_date.value )
print ( folder_obj.release_status.value )
print ( folder_obj.share_range.value )
print ( folder_obj.share_url.value )
print ( folder_obj.thumbnail_url.value )
