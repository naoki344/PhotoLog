from enum import Enum
import copy
'''
Value Object : ShareRange
'''


class ShareRange(Enum):
    PRIVATE = 1
    PUBLIC = 2
    PASSFRASE = 3


'''
Value Object : ShareUrl
'''


class ShareUrl:
    def __init__(self, share_url):
        self.value = share_url


'''
Value Object : Passfrase
'''


class SharePassword:
    def __init__(self, share_password):
        self.value = share_password


class Share:
    def __init__(self, share_range: ShareRange, share_password: SharePassword):

        self.share_range = share_range
        self.share_password = share_password

    def to_dict(self):
        return {
            "share_range": self.share_range.name,
            "share_password": self.share_password.value,
        }

    def modify(self, dict_data) -> 'Share':
        new_share = copy.deepcopy(self)

        if dict_data.get('share_range') is not None:
            new_share.share_range = ShareRange[dict_data['share_range']]

        if dict_data.get('share_password') is not None:
            new_share.share_password = SharePassword(
                dict_data['share_password'])

        return new_share

    @staticmethod
    def from_dict(dict_data: dict) -> 'Share':
        return Share(
            share_range=ShareRange[dict_data["share_range"]],
            share_password=SharePassword(dict_data["share_password"]),
        )
