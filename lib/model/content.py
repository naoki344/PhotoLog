from abc import ABC
from abc import ABCMeta, abstractmethod


class ContentID(ABC):
    def __init__(self, content_id):
        self.value = content_id

    def check_content_type(self):
        split_id_list = self.value.split('-')
        content_type = split_id_list[0]
        return content_type


class Content(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_content_id(self):
        pass

    @abstractmethod
    def get_content_type(self):
        return self.content_id.check_content_type()

    @staticmethod
    def check_content_type(content_id: ContentID):
        return content_id.check_content_type()


class ContentList():
    def __init__(self, content_obj_list):
        self.content_list = content_obj_list

    def add_content(self, content: Content):
        self.content_list.append(content)

    def to_dict(self):
        content_dict_list = []
        for content_obj in self.content_list:
            content_dict_list.append(content_obj.to_dict())

        return content_dict_list
