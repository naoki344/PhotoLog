# -*- coding: utf-8 -*-

import pprint
import json
import sys,os
from app.application.folder import GetAllFolderService
from lib.model.folder import FolderAuthorID

class GetUserAllFolder():

    def __init__( self, folder_author_id : FolderAuthorID ):
        self.folder = GetAllFolderService(folder_author_id)
       	
    def get_json(self,):
        self.all_folder = []
        for folder_obj in self.folder.folders :
            self.all_folder.append( folder_obj.to_dict() )
        json_txt = json.dumps( self.all_folder ,indent=4)
        return json_txt
