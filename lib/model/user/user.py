from datetime import datetime
from enum import Enum

from flask_login import UserMixin


class UserID:
    def __init__(self, value: str):
        self.value = value


class Password:
    def __init__(self, value: str):
        self.value = value

    def auth(self, imput_password):
        password_hash = imput_password
        if password_hash == self.value:
            return True
        return False


class Name:
    def __init__(self, value):
        self.value = value
        self.first_name = value
        self.last_name = value


class NickName:
    def __init__(self, value: str):
        self.value = value


class BirthDay:
    def __init__(self, value: datetime):
        self.value = value


class Gender(Enum):
    MAN = 1
    WOMAN = 2
    MIXGENDER = 3


class TermsStatus(Enum):
    DISAGREE = 0
    AGREE = 1


class UserType(Enum):
    FREE = 0
    PAID = 1


class RegisterDate:
    def __init__(self, value: datetime):
        self.value = value


class LastUpdateDate:
    def __init__(self, value: datetime):
        self.value = value


class PostalCode:
    def __init__(self, value: str):
        self.value = value


class Prefecture:
    def __init__(self, value: str):
        self.value = value


class City:
    def __init__(self, value: str):
        self.value = value


class HouseNumber:
    def __init__(self, value: str):
        self.value = value


class BuildingNumber:
    def __init__(self, value: str):
        self.value = value


class Address:
    def __init__(self, postal_code: PostalCode, prefecture: Prefecture,
                 city: City, house_number: HouseNumber,
                 building_number: BuildingNumber):

        self.postal_code = postal_code
        self.prefecture = prefecture
        self.city = city
        self.house_number = house_number
        self.building_number = building_number

    @staticmethod
    def from_dict(dict_data: dict) -> 'Folder':
        return Address(
            postal_code=PostalCode(dict_data['postal_code']),
            prefecture=Prefecture(dict_data['prefecture']),
            city=City(dict_data['city']),
            house_number=HouseNumber(dict_data['house_number']),
            building_number=BuildingNumber(dict_data['building_number']))


class EmailAddress:
    def __init__(self, value: str):
        self.value = value


class PhoneNumber:
    def __init__(self, value: str):
        self.value = value


class Contact:
    def __init__(self, address: Address, email_address: EmailAddress,
                 phone_number: PhoneNumber):

        self.address = address
        self.email_address = email_address
        self.phone_number = phone_number

    @staticmethod
    def from_dict(dict_data: dict) -> 'Contact':
        return Contact(
            address=Address.from_dict(dict_data),
            email_address=EmailAddress(dict_data['user_id']),
            phone_number=PhoneNumber(dict_data['phone_number']),
        )


class User(UserMixin):
    def __init__(self, user_id: UserID, password: Password, name: Name,
                 nick_name: NickName, birthday: BirthDay, contact: Contact,
                 gender: Gender, terms_status: TermsStatus,
                 user_type: UserType, register_date: RegisterDate,
                 last_update_date: LastUpdateDate):

        self.user_id = user_id
        self.password = password
        self.name = name
        self.nick_name = nick_name
        self.birthday = birthday
        self.contact = contact
        self.gender = gender
        self.terms_status = terms_status
        self.user_type = user_type
        self.register_date = register_date
        self.last_update_date = last_update_date
        self.authentication = False

    def auth(self, imput_password):
        if self.password.auth(imput_password):
            self.authentication = True

        return self.authentication

    def set_authenticated(self):
        self.authentication = True

    def is_authenticated(self):
        return self.authentication

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.user_id.value

    @staticmethod
    def from_dict(dict_data: dict) -> 'Folder':
        return User(
            user_id=UserID(dict_data['user_id']),
            password=Password(dict_data['password']),
            name=Name(dict_data['name']),
            nick_name=NickName(dict_data['nick_name']),
            birthday=BirthDay(dict_data['birthday']),
            contact=Contact.from_dict(dict_data),
            gender=Gender[dict_data['gender']],
            terms_status=TermsStatus[dict_data['terms_status']],
            user_type=UserType[dict_data['user_type']],
            register_date=RegisterDate(dict_data['register_date']),
            last_update_date=LastUpdateDate(dict_data['last_update_date']))
