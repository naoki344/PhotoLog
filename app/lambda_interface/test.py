# -*- coding: utf-8 -*-

import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../')
from app.application.folder import GetUserAllFolderService
from lib.model.folder.folder import FolderAuthorID

folder_author_id = 1
folder_service = GetUserAllFolderService(folder_author_id)
json_txt = folder_service.get_all_folder()
print (json_txt.encode("UTF-8") )
