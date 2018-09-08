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
        folder = Folder()
        print ( vars( folder ) )

    def get_db_data( self, query, parameter ):
        db = mysql.connector.connect(**self.config)
        cursor = db.cursor()
        cursor.execute(query, parameter)
        data = cursor.fetchall()
        cursor.close()
        db.close()
        return data
