# -*- coding: utf-8 -*-

import time
import uuid
from datetime import datetime

from lib.model.share.share import Share
from lib.model.share.share import ShareRange
from lib.model.share.share import ShareUrl
from lib.model.share.share import SharePassword


class ShareFactory():
    @staticmethod
    def create(dict_data) -> Share:
        if dict_data.get('share_range') is None:
            dict_data['share_range'] = 'PRIVATE'

        if dict_data.get('share_password') is None:
            dict_data['share_password'] = ''

        return _to_share_obj(dict_data)


def _to_share_obj(dict_data):
    data = [
        ShareRange[dict_data["share_range"]],
        SharePassword(dict_data["share_password"]),
    ]
    Share_obj = Share(*data)
    return Share_obj
