import uuid
import time
from datetime import datetime

from lib.model.file.file import File
from lib.model.file.file import FileID
from lib.model.file.file import FileType
from lib.model.file.file import Location
from lib.model.file.file import RegisterDate
from lib.model.file.file import LastUpdateDate
from lib.model.file.file import Name


class FileFactory:
    @staticmethod
    def create_by_system(file_name_str: str, location: Location):
        now_time = datetime.now()
        last_update_date = LastUpdateDate(now_time)
        register_date = RegisterDate(now_time)
        file_id = FileID('file-' + str(uuid.uuid4()))
        file_name = Name(file_name_str)
        file_type = FileType.get_by_name(file_name)
        return File(
            file_id=file_id,
            name=file_name,
            location=location,
            file_type=file_type,
            register_date=register_date,
            last_update_date=last_update_date)
