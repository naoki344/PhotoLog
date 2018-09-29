#!/usr/bin/python

import os
from os.path import dirname, join

import mysql.connector
from dotenv import load_dotenv

env_file_path = join(dirname(__file__), '../app/.env')
load_dotenv(env_file_path)
db_user = os.environ.get("PL_DB_USER")
db_password = os.environ.get("PL_DB_PASSWORD")
db_hostname = os.environ.get("PL_DB_HOSTNAME")
db_name = os.environ.get("PL_DB_NAME")

config = {
    'user': db_user,
    'password': db_password,
    'host': db_hostname,
    'database': db_name
}

db = mysql.connector.connect(**config)
sql = """
    CREATE TABLE IF NOT EXISTS folder (
        folder_id varchar(100) PRIMARY KEY NOT NULL,
        author_id varchar(100) DEFAULT NULL,
        name varchar(50) NOT NULL DEFAULT '',
        description varchar(500) NOT NULL DEFAULT '',
        register_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
        last_update_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        release_status INT NOT NULL DEFAULT 0,
        share_range INT NOT NULL DEFAULT 0,
        share_url VARCHAR(8190) NOT NULL DEFAULT '',
        thumbnail_url VARCHAR(8190) NOT NULL DEFAULT '',
        delete_flag INT NOT NULL DEFAULT 0
    );"""
cursor = db.cursor()
cursor.execute(sql)
cursor.close()

sql = """
    CREATE TABLE IF NOT EXISTS page (
        page_id varchar(100) PRIMARY KEY NOT NULL,
        author_id varchar(100) DEFAULT NULL,
        name varchar(50) NOT NULL DEFAULT '',
        description varchar(500) NOT NULL DEFAULT '',
        register_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
        last_update_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        release_status INT NOT NULL DEFAULT 0,
        share_range INT NOT NULL DEFAULT 0,
        share_url VARCHAR(8190) NOT NULL DEFAULT '',
        thumbnail_url VARCHAR(8190) NOT NULL DEFAULT '',
        delete_flag INT NOT NULL DEFAULT 0
    );"""
cursor = db.cursor()
cursor.execute(sql)
cursor.close()

sql = """
    CREATE TABLE IF NOT EXISTS album (
        album_id varchar(100) PRIMARY KEY NOT NULL,
        author_id varchar(100) DEFAULT NULL,
        name varchar(50) NOT NULL DEFAULT '',
        description varchar(500) NOT NULL DEFAULT '',
        register_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
        last_update_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        release_status INT NOT NULL DEFAULT 0,
        share_range INT NOT NULL DEFAULT 0,
        share_url VARCHAR(8190) NOT NULL DEFAULT '',
        thumbnail_url VARCHAR(8190) NOT NULL DEFAULT '',
        delete_flag INT NOT NULL DEFAULT 0
    );"""
cursor = db.cursor()
cursor.execute(sql)
cursor.close()

#cursor = db.cursor()
#sql = "select * from test WHERE id = %s"
#val = 1;
#cursor.execute(sql , ( val, ))
#for ( id_name, id_val ) in cursor:
#    print("{} = {} ".format( id_name, id_val ))
#
#cursor.close()
db.close()
