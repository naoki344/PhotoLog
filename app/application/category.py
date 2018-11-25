from app.infrastructure.category import CategoryDataSource
from app.infrastructure.category_link import CategoryFolderLinkDataSource
from lib.model.category.category import CategoryID


class CategoryCommandService:
    def __init__(self):
        self.category_datasource = CategoryDataSource()
        self.category_folder_link_datasource = CategoryFolderLinkDataSource()

    def link_folder(self, category, folder):
        return self.category_folder_link_datasource.link_folder(
            category.category_id, folder.folder_id)

    def unlink_folder(self, category, folder):
        return self.category_folder_link_datasource.unlink_folder(
            category.category_id, folder.folder_id)


class CategoryQueryService:
    def __init__(self):
        self.category_datasource = CategoryDataSource()
        self.category_folder_link_datasource = CategoryFolderLinkDataSource()

    def find_linked_folder(self, category_id: CategoryID):
        return self.category_folder_link_datasource.find_linked_folder(
            category_id)

    def find(self, category_id: CategoryID):
        category = self.category_datasource.find(category_id)
        if category == None:
            return None
        return category
