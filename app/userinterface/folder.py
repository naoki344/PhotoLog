# -*- coding: utf-8 -*-

import pprint
import json
import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
from application.folder import GetAllFolderService
from model.folder import FolderAuthorID

class GetUserAllFolder():

    def __init__( self, folder_author_id : FolderAuthorID ):
        folder = GetAllFolderService(folder_author_id)
        self.all_folder = []
        for folder_obj in folder.folders :
            self.all_folder.append( folder_obj.to_dict() )
        json_txt = json.dumps( self.all_folder ,indent=4)

        return json_txt
