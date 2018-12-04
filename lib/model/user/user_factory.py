# -*- coding: utf-8 -*-
from datetime import datetime

from lib.model.user.user import User
from lib.model.user.user import UserID
from lib.model.user.user import Password
from lib.model.user.user import Name
from lib.model.user.user import NickName
from lib.model.user.user import BirthDay
from lib.model.user.user import Gender
from lib.model.user.user import TermsStatus
from lib.model.user.user import UserType
from lib.model.user.user import RegisterDate
from lib.model.user.user import LastUpdateDate
from lib.model.user.user import PostalCode
from lib.model.user.user import Prefecture
from lib.model.user.user import City
from lib.model.user.user import HouseNumber
from lib.model.user.user import BuildingNumber
from lib.model.user.user import Address
from lib.model.user.user import EmailAddress
from lib.model.user.user import PhoneNumber
from lib.model.user.user import Contact


class UserFactory():
    def create(self, dict_data) -> User:

        if dict_data.get('user_id') == None:
            return False

        if dict_data.get('password') == None:
            return False

        if dict_data.get('name') == None:
            return False

        if dict_data.get('nick_name') == None:
            return False

        if dict_data.get('birthday') == None:
            now_time = datetime.now()
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

        return self._to_user_obj(dict_data)

    def _to_user_obj(self, dict_data):
        now_time = datetime.now()
        password = Password.create_hashpw(dict_data['password'])
        address = Address(
            postal_code=PostalCode(dict_data['postal_code']),
            prefecture=Prefecture(dict_data['prefecture']),
            city=City(dict_data['city']),
            house_number=HouseNumber(dict_data['house_number']),
            building_number=BuildingNumber(dict_data['building_number']))
        contact = Contact(
            address=address,
            email_address=EmailAddress(dict_data['user_id']),
            phone_number=PhoneNumber(dict_data['phone_number']))
        return User(
            user_id=UserID(dict_data['user_id']),
            password=password,
            name=Name(dict_data['name']),
            nick_name=NickName(dict_data['nick_name']),
            birthday=BirthDay(dict_data['birthday']),
            contact=contact,
            gender=Gender[dict_data['gender']],
            terms_status=TermsStatus[dict_data['terms_status']],
            user_type=UserType[dict_data['user_type']],
            register_date=RegisterDate(now_time),
            last_update_date=LastUpdateDate(now_time))
