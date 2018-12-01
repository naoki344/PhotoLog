import glob
import os
import cv2

from lib.model.file.file import Location
from lib.model.file.file import File
from lib.model.file.file import ShapeSize
from lib.model.file.file import Width
from lib.model.file.file import Height
from lib.model.file.file_factory import FileFactory
from lib.model.file.file_list import FileList


class LocalStorageDataSource:
    def __init__(self):
        pass

    def find_dir_files(self, location: Location):
        target = '{}/*'.format(location.path.value)
        file_name_list = glob.glob(target)
        file_list = FileList([])
        for file_full_path in file_name_list:
            img = cv2.imread(file_full_path)
            h, w, _ = img.shape
            width = Width(w)
            height = Height(h)
            shape_size = ShapeSize(width=width, height=height)
            file_name_str = os.path.basename(file_full_path)
            file = FileFactory.create_by_system(
                file_name_str=file_name_str,
                location=location,
                shape_size=shape_size)
            file_list.add_file(file)
        return file_list
