#!/usr/bin/python

import mysql.connector

from app.util import get_db_config
from app.util import get_db_prefix


class DataSource():
    def __init__(self):
        self.config = get_db_config()

    def get(self, query, parameter, dict_flag):
        db = mysql.connector.connect(**self.config)
        if dict_flag == True:
            cursor = db.cursor(dictionary=True)
        else:
            cursor = db.cursor()

        cursor.execute(query, parameter)
        data = cursor.fetchall()
        cursor.close()
        db.close()
        return data

    def insert(self, query, parameter, dict_flag):
        db = mysql.connector.connect(**self.config)
        if dict_flag == True:
            cursor = db.cursor(dictionary=True)
        else:
            cursor = db.cursor()

        try:
            data = cursor.execute(query, parameter)
            get_id_query = 'SELECT LAST_INSERT_ID();'
            parameter = []
            cursor.execute(get_id_query, parameter)
            data = cursor.fetchall()
            db.commit()
            row_id = data[0]["LAST_INSERT_ID()"]
        except:
            db.rollback()
            raise

        cursor.close()
        db.close()
        return row_id

    def update(self, query, parameter, dict_flag):
        db = mysql.connector.connect(**self.config)
        if dict_flag == True:
            cursor = db.cursor(dictionary=True)
        else:
            cursor = db.cursor()

        try:
            data = cursor.execute(query, parameter)
            db.commit()
        except:
            db.rollback()
            raise

        cursor.close()
        db.close()
        return True

    def get_prefix(self):
        return get_db_prefix()
