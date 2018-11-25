import json
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../')

from app.application.file import FileCommandService
from app.application.file import FileSystemStorageService
from app.application.folder import FolderCommandService
from lib.model.folder.folder_factory import FolderFactory
from lib.model.file.file import File
from lib.model.file.file import Location
from lib.model.file.file import StorageType
from lib.model.file.file import Path
from lib.model.file.file import Name
from lib.model.file.file_list import FileList


def RegisterFileInterface(dir_path):
    file_system_storage_service = FileSystemStorageService()
    file_command_service = FileCommandService()

    location = Location(
        storage_type=StorageType['LOCAL_DIRECTORY'], path=Path(dir_path))
    # ファイルの一覧を取得
    file_list = file_system_storage_service.find_by_location(location)
    # フォルダを作成
    dirname = os.path.basename(dir_path)
    data = {
        "info": {
            "author_id": "miyoshi@example.com",
            "name": dirname,
        },
        "share": {
            "share_range": "PRIVATE"
        }
    }
    folder_factory = FolderFactory()
    folder_obj = folder_factory.create(data)
    if folder_obj is False:
        txt = 'folder can not create'
        return txt.encode("UTF-8")

    folder_command_service = FolderCommandService()
    folder = folder_command_service.register(folder_obj)

    # ファイルを登録
    file_command_service.register_list(folder, file_list)


RegisterFileInterface(
    '/Users/miyoshi_naoki/pjct/PhotoLog/PhotoLog/file/sample01')
