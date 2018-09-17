# -*- coding: utf-8 -*-

from app.application.folder import GetUserAllFolderService
from lib.model.folder.folder import FolderAuthorID

class GetUserAllFolder():

    def __init__( self, folder_author_id : FolderAuthorID ):
        folder_service = GetUserAllFolderService(folder_author_id)
        self.user_folder_list = folder_service.get_all_folder()

    def get_json(self):
        json_txt = self.user_folder_list.to_dict()
        return json_txt
