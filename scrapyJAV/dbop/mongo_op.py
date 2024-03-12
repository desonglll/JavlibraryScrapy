# -*- coding: utf-8 -*-
"""
File: mongo_op
Description: 
Author: mikeshinoda
Date: 2024/3/12
"""
from pymongo import MongoClient


# TODO: Add your code here
# FINISH: Add your code here
# FIXME: Add your code here

def init_database():
    conn = MongoClient('mongodb://localhost:27017')
    db = conn.scrapy
    db.get_collection("works").drop()
    print("Initialized Mongo database")
