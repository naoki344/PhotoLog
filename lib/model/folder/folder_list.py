# -*- coding: utf-8 -*-
from enum import Enum
import json
import datetime
from lib.model.folder.folder import Folder

class FolderList():

    def __init__( self, folder_obj_list ):
        self.uset_folder_list = folder_obj_list

    def add_folder( self, folder : Folder ):
        self.uset_folder_list.append( folder )

    def to_dict(self):
        self.folder_list = []
        for folder_obj in self.uset_folder_list :
            self.folder_list.append( folder_obj.to_dict() )

        self.json_txt = json.dumps( self.folder_list ,indent=4)
        return self.json_txt
