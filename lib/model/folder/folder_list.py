# -*- coding: utf-8 -*-
from enum import Enum
import datetime
from lib.model.folder.folder import Folder

class FolderList():

    def __init__( self, folder_obj_list ):
        self.folder_list = folder_obj_list

    def add_folder( self, folder : Folder ):
        self.folder_list.append( folder )

    def to_dict(self):
        folder_dict_list = []
        for folder_obj in self.folder_list :
            folder_dict_list.append( folder_obj.to_dict() )

        return folder_dict_list
