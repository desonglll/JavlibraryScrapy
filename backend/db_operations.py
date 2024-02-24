# -*- coding: utf-8 -*-
"""
File: db_operations
Description: 
Author: mikeshinoda
Date: 2024/2/18
"""

# TODO: Add your code here
# FINISH: Add your code here
# FIXME: Add your code here
# db_operations.py

import pymysql
from contextlib import contextmanager
from db_op.tools import get_config, get_mysql_db_name


@contextmanager
def get_db_connection():
    connection = pymysql.connect(**get_config("mysql_config"))
    try:
        yield connection
    finally:
        connection.close()


# 查询 works_table 的条目数
def get_works_table_count():
    with get_db_connection() as conn:
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(f"use {get_mysql_db_name()};")
        cursor.execute("SELECT COUNT(*) FROM works_table  WHERE genres LIKE '%单体%' AND genres NOT LIKE '%VR%'")
        result = cursor.fetchone()
        return result["COUNT(*)"]


def fetch_data_from_db(query, args=None):
    with get_db_connection() as conn:
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(f"use {get_mysql_db_name()};")
        cursor.execute(query, args)
        return cursor.fetchall()
