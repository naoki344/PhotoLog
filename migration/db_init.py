#!/usr/bin/python

import os
from os.path import join, dirname
from dotenv import load_dotenv
import mysql.connector

env_file_path = join(dirname(__file__), '../app/.env')
load_dotenv(env_file_path)
db_user     = os.environ.get("PL_DB_USER")
db_password = os.environ.get("PL_DB_PASSWORD")
db_hostname = os.environ.get("PL_DB_HOSTNAME")
db_name     = os.environ.get("PL_DB_NAME")

config = {
    'user' : db_user,
    'password' : db_password,
    'host' : db_hostname,
    'database' : db_name
}

db = mysql.connector.connect(**config)
sql = """
    CREATE TABLE IF NOT EXISTS folder (
        folder_ID BIGINT PRIMARY KEY NOT NULL AUTO_INCREMENT,
        author_ID int DEFAULT NULL,
        name varchar(50) NOT NULL DEFAULT '',
        description varchar(500) NOT NULL DEFAULT '',
        register_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
        last_update_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        release_status INT NOT NULL DEFAULT 0,
        share_range INT NOT NULL DEFAULT 0,
        share_url VARCHAR(8190) NOT NULL DEFAULT '',
        thumbnail_url VARCHAR(8190) NOT NULL DEFAULT ''
    );"""
cursor = db.cursor()
cursor.execute(sql)
cursor.close()

sql = """
    CREATE TABLE IF NOT EXISTS page (
        page_ID BIGINT PRIMARY KEY NOT NULL AUTO_INCREMENT,
        author_ID int DEFAULT NULL,
        name varchar(50) NOT NULL DEFAULT '',
        description varchar(500) NOT NULL DEFAULT '',
        register_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
        last_update_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        release_status INT NOT NULL DEFAULT 0,
        share_range INT NOT NULL DEFAULT 0,
        share_url VARCHAR(8190) NOT NULL DEFAULT '',
        thumbnail_url VARCHAR(8190) NOT NULL DEFAULT ''
    );"""
cursor = db.cursor()
cursor.execute(sql)
cursor.close()


sql = """
    CREATE TABLE IF NOT EXISTS album (
        album_ID BIGINT PRIMARY KEY NOT NULL AUTO_INCREMENT,
        author_ID int DEFAULT NULL,
        name varchar(50) NOT NULL DEFAULT '',
        description varchar(500) NOT NULL DEFAULT '',
        register_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
        last_update_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        release_status INT NOT NULL DEFAULT 0,
        share_range INT NOT NULL DEFAULT 0,
        share_url VARCHAR(8190) NOT NULL DEFAULT '',
        thumbnail_url VARCHAR(8190) NOT NULL DEFAULT ''
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
