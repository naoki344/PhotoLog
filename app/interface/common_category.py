# -*- coding: utf-8 -*-

import json

import flask_login
from flask import Blueprint
from flask import request

from app.application.common_category import CommonCategoryCommandService
from app.application.common_category import CommonCategoryQueryService
from lib.model.category.category import CategoryID
from lib.model.info.info import AuthorID
from lib.model.category.category import CategoryType
from lib.model.category.category_factory import CategoryFactory
from lib.model.user.user import User

app_common_category = Blueprint('app_common_category', __name__)

# main で登録されているPATHからの相対パスで以下のURLを指定する
#  以下の場合のPATHは、/photo_log/common_category/file になる
#  - main.py のregister_blueprint が url_prefix='/photo_log/common_category'
#  - @app_common_category.route('/file')


@app_common_category.route('/', methods=['GET', 'POST'])
# @flask_login.login_required
def common_category_index(user_id):

    common_category_author_id = user_id
    if request.method == 'GET':
        common_category_query_service = CommonCategoryQueryService()
        user_common_category_list = common_category_query_service.find_user_all(
            AuthorID(common_category_author_id))
        common_category_dict_list = user_common_category_list.to_dict()
        json_txt = json.dumps(common_category_dict_list, indent=4)
        return json_txt.encode("UTF-8")

    if request.method == 'POST':
        post_data = request.json
        data = post_data.copy()
        data['category_type'] = CategoryType.COMMON.name
        category_factory = CategoryFactory()
        common_category_obj = category_factory.create(data)
        if common_category_obj is False:
            txt = 'common_category can not create'
            return txt.encode("UTF-8")

        common_category_command_service = CommonCategoryCommandService()
        registerd_common_category = common_category_command_service.register(
            common_category_obj)

        common_category_dict = registerd_common_category.to_dict()
        json_txt = json.dumps(common_category_dict, indent=4)
        return json_txt.encode("UTF-8")


@app_common_category.route(
    '/<path:common_category_id>', methods=['GET', 'PUT', 'DELETE'])
# @flask_login.login_required
def common_category(user_id, common_category_id):
    common_category_author_id = user_id
    if request.method == 'GET':
        common_category_query_service = CommonCategoryQueryService()
        common_category_obj = common_category_query_service.find(
            CategoryID(common_category_id))
        if common_category_obj is None:
            txt = 'common_category do not exist'
            return txt.encode("UTF-8")

        common_category_dict = common_category_obj.to_dict()
        json_txt = json.dumps(common_category_dict, indent=4)
        return json_txt.encode("UTF-8")

    if request.method == 'PUT':
        post_data = request.json

        common_category_query_service = CommonCategoryQueryService()
        org_common_category = common_category_query_service.find(
            CategoryID(common_category_id))
        if org_common_category is None:
            txt = 'common_category do not exist'
            return txt.encode("UTF-8")

        new_common_category = org_common_category.modify(post_data)

        common_category_command_service = CommonCategoryCommandService()
        updated_common_category = common_category_command_service.update(
            org_common_category, new_common_category)

        common_category_dict = updated_common_category.to_dict()
        json_txt = json.dumps(common_category_dict, indent=4)
        return json_txt.encode("UTF-8")

    if request.method == 'DELETE':
        post_data = request.json

        common_category_query_service = CommonCategoryQueryService()
        org_common_category = common_category_query_service.find(
            CategoryID(common_category_id))

        common_category_command_service = CommonCategoryCommandService()
        try:
            deleted_common_category = common_category_command_service.delete(
                org_common_category)
        except:
            msg = 'common_category[' + org_common_category.common_category_id.value + '] delete is failuer'
            return msg.encode("UTF-8")

        json_txt = json.dumps(deleted_common_category, indent=4)
        return json_txt.encode("UTF-8")
