# -*- coding: utf-8 -*-

from lib.model.user.user import User
from lib.model.user.user import UserID

from .datasource import DataSource


class UserDataSource:
    def __init__(self):
        self.datasource = DataSource()
        self.db_prefix = self.datasource.get_prefix()

    def find(self, user_id: UserID):
        sql = 'SELECT * FROM {}_user WHERE user_id=%s;'.format(self.db_prefix)
        parameter = [user_id.value]
        users = self.datasource.get(sql, parameter, True)
        if len(users) == 0:
            return None

        user_row = users[0]
        user_obj = self._to_user_obj(user_row)
        return user_obj

    def _to_user_obj(self, user_row):
        user_obj = User.from_dict(user_row)
        return user_obj
