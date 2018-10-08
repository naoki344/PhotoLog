# -*- coding: utf-8 -*-
from datetime import datetime

from lib.model.user.user import Password
from lib.model.user.user import User


class UserFactory():
    def create(self, dict_data) -> User:
        now_time = datetime.now()

        if dict_data.get('user_id') == None:
            return False

        if dict_data.get('password') == None:
            return False
        else:
            dict_data['password'] = Password.create_hashpw(
                dict_data['password'])

        if dict_data.get('name') == None:
            return False

        if dict_data.get('nick_name') == None:
            return False

        if dict_data.get('birthday') == None:
            dict_data['birthday'] = now_time

        if dict_data.get('terms_status') == None:
            return False

        if dict_data.get('gender') == None:
            return False

        if dict_data.get('user_type') == None:
            return False

        if dict_data.get('phone_number') == None:
            return False

        if dict_data.get('postal_code') == None:
            return False

        if dict_data.get('prefecture') == None:
            return False

        if dict_data.get('city') == None:
            return False

        if dict_data.get('house_number') == None:
            return False

        if dict_data.get('building_number') == None:
            return False

        dict_data['register_date'] = now_time
        dict_data['last_update_date'] = now_time

        return self._to_user_obj(dict_data)

    def _to_user_obj(self, dict_data):
        return User.from_dict(dict_data)
