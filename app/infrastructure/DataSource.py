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

    def get_row( self, table_name, where_array ):
        db = mysql.connector.connect(**self.config)
        cursor = db.cursor()
        #val_array = [ table_name ]
        val_array = []
        sql = "select * from " + table_name
        for key,value in where_array.items():
            sql = sql + " WHERE "
            sql = sql + key + "=" + value
        #    val_array.append( key )
        #    val_array.append( value )

        print ( sql )
        #cursor.execute(sql , tuple(val_array) )
        cursor.execute(sql)
        row = cursor.fetchall()
        print( *row,sep='\n' )
        cursor.close()
        db.close()


datasource = DataSource()
datasource.get_row('folder', { 'folder_ID' : 1})

