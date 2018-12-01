from .datasource import DataSource
from lib.model.file.file import File
from lib.model.file.file import FileID
from lib.model.file.file_list import FileList
from lib.model.folder.folder import Folder


class FileDataSource:
    def __init__(self):
        self.datasource = DataSource()
        self.db_prefix = self.datasource.get_prefix()

    def register(self, folder, file):
        sql = 'INSERT INTO {}_file(file_id,folder_id,name,file_type,storage_type,path,width,height,register_date,last_update_date) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ;'.format(
            self.db_prefix)
        parameter = [
            file.file_id.value,
            folder.folder_id.value,
            file.name.value,
            file.file_type.name,
            file.location.storage_type.name,
            file.location.path.value,
            file.shape_size.width.value,
            file.shape_size.height.value,
            file.register_date.value,
            file.last_update_date.value,
        ]
        folder_id = self.datasource.insert(sql, parameter, True)

        return True

    def register_list(self, folder, file_list):
        for file in file_list.file_list:
            self.register(folder, file)

        return True

    def find_by_folder(self, folder: Folder):
        sql = 'SELECT * FROM {}_file WHERE folder_id=%s;'.format(
            self.db_prefix)
        parameter = [folder.folder_id.value]
        files = self.datasource.get(sql, parameter, True)
        if len(files) == 0:
            return None

        file_list = FileList([])
        for file_row in files:
            file_obj = File.from_dict(file_row)
            file_list.add_file(file_obj)

        return file_list

    def find(self, file_id: FileID):
        sql = 'SELECT * FROM {}_file WHERE file_id=%s;'.format(self.db_prefix)
        parameter = [file_id.value]
        files = self.datasource.get(sql, parameter, True)
        if len(files) == 0:
            return None
        file_row = files[0]
        return File.from_dict(file_row)
