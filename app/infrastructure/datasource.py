#!/usr/bin/python

import os
from os.path import join, dirname
from dotenv import load_dotenv
import mysql.connector



class DataSource():
    def __init__(self):
        env_file_path = join(dirname(__file__), '../.env')
        load_dotenv(env_file_path)
        db_user     = os.environ.get("PL_DB_USER")
        db_password = os.environ.get("PL_DB_PASSWORD")
        db_hostname = os.environ.get("PL_DB_HOSTNAME")
        db_name     = os.environ.get("PL_DB_NAME")
        self.config = {
            'user' : db_user,
            'password' : db_password,
            'host' : db_hostname,
            'database' : db_name
        }

    def get_db_data( self, query, parameter, dict_flag ):
        db = mysql.connector.connect(**self.config)
        if dict_flag == True :
            cursor = db.cursor(dictionary=True)
        else :
            cursor = db.cursor()

        cursor.execute(query, parameter)
        data = cursor.fetchall()
        cursor.close()
        db.close()
        return data

    def insert_db( self, query, parameter, dict_flag ):
        db = mysql.connector.connect(**self.config)
        if dict_flag == True :
            cursor = db.cursor(dictionary=True)
        else :
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

    def update_db_data( self, query, parameter, dict_flag ):
        db = mysql.connector.connect(**self.config)
        print( parameter )
        if dict_flag == True :
            cursor = db.cursor(dictionary=True)
        else :
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
