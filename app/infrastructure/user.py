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

    def register(self, user: User):
        sql = 'INSERT INTO {}_user(user_id,password,name,nick_name,birthday,register_date,last_update_date,terms_status,gender,user_type,phone_number,postal_code,prefecture,city,house_number,building_number) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'.format(
            self.db_prefix)
        dict_data = user.to_sql_dict()
        parameter = [
            dict_data['user_id'], dict_data['password'], dict_data['name'],
            dict_data['nick_name'], dict_data['birthday'],
            dict_data['register_date'], dict_data['last_update_date'],
            dict_data['terms_status'], dict_data['gender'],
            dict_data['user_type'], dict_data['phone_number'],
            dict_data['postal_code'], dict_data['prefecture'],
            dict_data['city'], dict_data['house_number'],
            dict_data['building_number']
        ]
        result = self.datasource.insert(sql, parameter, True)
        if result != True:
            return False
        return True

    def _to_user_obj(self, user_row):
        user_obj = User.from_dict(user_row)
        return user_obj
