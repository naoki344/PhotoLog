#!/usr/bin/python

import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')

import mysql.connector

from app.util import get_db_config
from app.util import get_db_prefix

config = get_db_config()
db_prefix = get_db_prefix()

db = mysql.connector.connect(**config)
sql = """
    CREATE TABLE IF NOT EXISTS %s_folder (
        folder_id varchar(100) PRIMARY KEY NOT NULL,
        author_id varchar(100) DEFAULT NULL,
        name varchar(50) NOT NULL DEFAULT '',
        description varchar(500) NOT NULL DEFAULT '',
        register_date DATETIME NOT NULL,
        last_update_date DATETIME NOT NULL,
        release_status varchar(20) DEFAULT NULL,
        share_range varchar(20) DEFAULT NULL,
        share_url VARCHAR(8190) NOT NULL DEFAULT '',
        thumbnail_url VARCHAR(8190) NOT NULL DEFAULT '',
        delete_status varchar(20) DEFAULT NULL
    );""" % db_prefix
cursor = db.cursor()
cursor.execute(sql)
cursor.close()

sql = """
    CREATE TABLE IF NOT EXISTS %s_category (
        category_id varchar(100) PRIMARY KEY NOT NULL,
        author_id varchar(100) DEFAULT NULL,
        name varchar(50) NOT NULL DEFAULT '',
        description varchar(500) NOT NULL DEFAULT '',
        register_date DATETIME,
        last_update_date DATETIME,
        release_status varchar(20) DEFAULT NULL,
        category_type varchar(20) DEFAULT NULL,
        share_range varchar(20) DEFAULT NULL,
        share_url VARCHAR(8190) NOT NULL DEFAULT '',
        thumbnail_url VARCHAR(8190) NOT NULL DEFAULT '',
        delete_status varchar(20) DEFAULT NULL
    );""" % db_prefix
cursor = db.cursor()
cursor.execute(sql)
cursor.close()

sql = """
    CREATE TABLE IF NOT EXISTS %s_album_content (
        album_id varchar(100) NOT NULL,
        content_id varchar(100) NOT NULL,
        content_type varchar(20) DEFAULT NULL,
        delete_status varchar(20) DEFAULT NULL,
        PRIMARY KEY(album_id,content_id)
    );""" % db_prefix
cursor = db.cursor()
cursor.execute(sql)
cursor.close()

sql = """
    CREATE TABLE IF NOT EXISTS %s_album (
        album_id varchar(100) PRIMARY KEY NOT NULL,
        author_id varchar(100) DEFAULT NULL,
        name varchar(50) NOT NULL DEFAULT '',
        description varchar(500) NOT NULL DEFAULT '',
        register_date DATETIME,
        last_update_date DATETIME,
        release_status varchar(20) DEFAULT NULL,
        share_range varchar(20) DEFAULT NULL,
        share_url VARCHAR(8190) NOT NULL DEFAULT '',
        thumbnail_url VARCHAR(8190) NOT NULL DEFAULT '',
        delete_status varchar(20) DEFAULT NULL
    );""" % db_prefix
cursor = db.cursor()
cursor.execute(sql)
cursor.close()

sql = """
    CREATE TABLE IF NOT EXISTS %s_user (
        user_id varchar(100) PRIMARY KEY NOT NULL,
        password varchar(200) DEFAULT NULL,
        name varchar(50) NOT NULL DEFAULT '',
        nick_name varchar(50) NOT NULL DEFAULT '',
        birthday DATETIME,
        register_date DATETIME,
        last_update_date DATETIME,
        terms_status varchar(20) DEFAULT NULL,
        gender varchar(20) NOT NULL DEFAULT '',
        user_type varchar(20) NOT NULL DEFAULT '',
        phone_number varchar(50) NOT NULL DEFAULT '',
        postal_code varchar(50) NOT NULL DEFAULT '',
        prefecture varchar(50) NOT NULL DEFAULT '',
        city varchar(50) NOT NULL DEFAULT '',
        house_number varchar(100) NOT NULL DEFAULT '',
        building_number varchar(100) NOT NULL DEFAULT ''
    );""" % db_prefix
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
