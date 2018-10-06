import os
from os.path import dirname
from os.path import join

from dotenv import load_dotenv

env_file_path = join(dirname(__file__), '.env')
load_dotenv(env_file_path)

db_user = os.environ.get("PL_DB_USER")
db_password = os.environ.get("PL_DB_PASSWORD")
db_hostname = os.environ.get("PL_DB_HOSTNAME")
db_name = os.environ.get("PL_DB_NAME")
db_stage = os.environ.get("PL_STAGE")


def get_db_config():
    return {
        'user': db_user,
        'password': db_password,
        'host': db_hostname,
        'database': db_name
    }


def get_db_prefix():
    return db_stage
