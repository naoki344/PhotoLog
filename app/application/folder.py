# -*- coding: utf-8 -*-

import pprint
import json
import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
from infrastructure.folder import FolderDataSource
from model.folder import FolderAuthorID

class GetUserAllFolder():

    def __init__( self, folder_author_id : FolderAuthorID ):
        fd = FolderDataSource()
        folders = fd.get_all_folder(folder_author_id)
        folder_dic_array = []
        for folder_obj in folders :
            folder_dic_array.append( folder_obj.to_dict() )

        #pprint.pprint ( folder_dic_array ,indent=4,depth=None)
        json_txt = json.dumps( folder_dic_array ,indent=4)
        print ( json_txt )

GetUserAllFolder(1)
