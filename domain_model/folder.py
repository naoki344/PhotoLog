# -*- coding: utf-8 -*-
import os
from enum import Enum
import datetime
from test_mod import *


'''
Value Object : ID
'''
class FolderAuthorID:
  def __init__( self,user_id ):
    self.value = 1

  def __check_exist_user(self):
    return True


'''
Value Object : Name
'''
class FolderName:

  def __init__( self,name ):
    self.value = name


'''
Value Object : Description
'''
class FolderDescription:

  def __init__( self,description_txt ):
    self.value = description_txt

  def __check_character_limit(self):
      return True;
    #文字数のチェック

'''
Value Object : LastUpdateDate
'''
class FolderLastUpdateDate:

  def __init__( self,date ):
    self.value = date


'''
Value Object : RegisterDate
'''
class FolderRegisterDate:

  def __init__( self,date ):
    self.value = date


'''
Value Object : ReleaseStatus
'''
class FolderReleaseStatus(Enum):
  OPEN = 1
  CLOSE = 2


'''
Value Object : ShareRange
'''
class FolderShareRange(Enum):
  PRIVATE = 1
  PUBLICK = 2
  PASSFRASE = 3


'''
Value Object : ShareUrl
'''
class FolderShareUrl:
  def __init__( self,share_url ):
    self.value = share_url


'''
Value Object : ThumbnailUrl
'''
class FolderThumbnailUrl:
  def __init__( self,thumbnail_url ):
    self.value = thumbnail_url

class Folder():

  def __init__( self,
               author_id : FolderAuthorID,
               name : FolderName,
               description : FolderDescription,
               last_update_date : FolderLastUpdateDate,
               register_date : FolderRegisterDate,
               release_status : FolderReleaseStatus,
               share_range : FolderShareRange,
               share_url : FolderShareUrl,
               thumbnail_url : FolderThumbnailUrl):

    self.author = FolderAuthorID( author_id )
    self.name = FolderName( name )
    self.description = FolderDescription( description )
    self.register_date = FolderRegisterDate( register_date )
    self.last_update_date = FolderLastUpdateDate( last_update_date )
    self.release_status = FolderReleaseStatus( release_status )
    self.share_range = FolderShareRange( share_range )
    self.share_url = FolderShareUrl( share_url )
    self.thumbnail_url = FolderThumbnailUrl( thumbnail_url )


# インスタンスの作成
folder_obj = Folder(1,'taro', '太郎のフォルダです', datetime.datetime.today(), datetime.datetime.today(), 1, 2,'https://share.url', 'https://thumbnail.url')
print ( folder_obj.author.value )
print ( folder_obj.name.value )
print ( folder_obj.description.value )
print ( folder_obj.last_update_date.value )
print ( folder_obj.register_date.value )
print ( folder_obj.release_status.value )
print ( folder_obj.share_range.name )
print ( folder_obj.share_url.value )
print ( folder_obj.thumbnail_url.value )

