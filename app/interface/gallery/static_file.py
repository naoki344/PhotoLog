import json

import flask_login
from flask import Blueprint
from flask import request

app_static = Blueprint(
    "app_static",
    __name__,
    static_url_path='/',
    static_folder='../../../gallery_page/dist/')
