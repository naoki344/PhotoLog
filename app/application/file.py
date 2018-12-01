# -*- coding: utf-8 -*-

import datetime
import json
import os
import sys

from app.infrastructure.file import FileDataSource
from app.infrastructure.local_storage import LocalStorageDataSource
from lib.model.folder.folder import Folder
from lib.model.file.file import File
from lib.model.file.file import FileID
from lib.model.file.file import Location
from lib.model.file.file_list import FileList


class FileCommandService:
    def __init__(self):
        self.file_datasource = FileDataSource()
        self.local_storage_datasource = LocalStorageDataSource()

    def register(self, folder: Folder, file: File):
        self.file_datasource.register(folder, file)

    def register_list(self, folder: Folder, file_list: FileList):
        self.file_datasource.register_list(folder, file_list)

    def create_thumbnail(self, file: File):
        pass


class FileQueryService:
    def __init__(self):
        self.file_datasource = FileDataSource()

    def find_by_folder(self, folder: Folder):
        file_list = self.file_datasource.find_by_folder(folder)
        return file_list

    def find(self, file_id: FileID):
        file = self.file_datasource.find(file_id)
        return file


class FileSystemStorageService:
    def __init__(self):
        self.local_storage_datasource = LocalStorageDataSource()

    def find_by_location(self, location: Location):
        file_list = self.local_storage_datasource.find_dir_files(location)
        return file_list
