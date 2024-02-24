# -*- coding: utf-8 -*-
"""
File: tools
Description: 
Author: mikeshinoda
Date: 2024/2/18
"""
import pymysql
# TODO: Add your code here
# FINISH: Add your code here
# FIXME: Add your code here
import yaml
import os


def get_config(key):
    with open(os.path.join(os.getcwd(), "config.yaml"), "r") as f:
        data = yaml.safe_load(f)
    return data[key]


def get_mysql_db_name():
    return get_config("mysql_db_name")


def get_db_cursor():
    connection = pymysql.connect(**get_config("mysql_config"))
    cursor = connection.cursor()
    return cursor
