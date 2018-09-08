#/usr/bin/python3

from enum import Enum
'''
Value Object : ID
'''
class AuthorID:
  def __init__( self,user_id ):
    self.value = 1

  def __check_exist_user(self):
    return True


'''
Value Object : Name
'''
class Name:

  def __init__( self,name ):
    self.value = name


'''
Value Object : Description
'''
class Description:

  def __init__( self,description_txt ):
    self.value = description_txt

  def __check_character_limit(self):
      return True;
    #文字数のチェック

'''
Value Object : LastUpdateDate
'''
class LastUpdateDate:

  def __init__( self,date ):
    self.value = date


'''
Value Object : RegisterDate
'''
class RegisterDate:

  def __init__( self,date ):
    self.value = date


'''
Value Object : ReleaseStatus
'''
class ReleaseStatus(Enum):
  OPEN = 1
  CLOSE = 2


'''
Value Object : ShareRange
'''
class ShareRange(Enum):
  PRIVATE = 1
  PUBLICK = 2
  PASSFRASE = 3


'''
Value Object : ShareUrl
'''
class ShareUrl:
  def __init__( self,share_url ):
    self.value = share_url


'''
Value Object : ThumbnailUrl
'''
class ThumbnailUrl:
  def __init__( self,thumbnail_url ):
    self.value = thumbnail_url
