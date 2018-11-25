import glob
import os

from lib.model.file.file import Location
from lib.model.file.file import File
from lib.model.file.file_factory import FileFactory
from lib.model.file.file_list import FileList


class LocalStorageDataSource:
    def __init__(self):
        pass

    def find_dir_files(self, location: Location):
        target = '{}/*'.format(location.path.value)
        file_name_list = glob.glob(target)
        file_list = FileList([])
        for file_name_str in file_name_list:
            file_name_str = os.path.basename(file_name_str)
            file = FileFactory.create_by_system(
                file_name_str=file_name_str, location=location)
            file_list.add_file(file)
        return file_list
