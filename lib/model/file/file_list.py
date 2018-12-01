# -*- coding: utf-8 -*-
from enum import Enum
import datetime
from lib.model.file.file import File


class FileList():
    def __init__(self, file_obj_list):
        self.file_list = file_obj_list

    def add_file(self, file: File):
        self.file_list.append(file)

    def to_dict(self):
        file_dict_list = []
        for file_obj in self.file_list:
            file_dict_list.append(file_obj.to_dict())

        return file_dict_list
