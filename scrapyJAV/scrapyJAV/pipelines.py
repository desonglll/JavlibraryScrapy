from collections import defaultdict

import pymysql
from pymongo import MongoClient

import scrapyJAV.config.database_config as db_config


class MongoDBPipeline:
    """
    auth: mikeshinoda
    date: 2024.3.11
    """

    def __init__(self):
        self.items_dict = defaultdict(list)

    def open_spider(self, spider):
        self.conn = MongoClient('mongodb://localhost:27017')
        self.db = self.conn.scrapy

    def process_item(self, item, spider):
        print(item)
        if True:
            # 构造要插入的文档
            document = {
                "title": item.get("title", ""),
                "release_date": item.get("release_date", ""),
                "serial_number": item.get("serial_number", ""),
                "genres": item.get("genres", []),
                "maker": item.get("maker", []),
                "cast": item.get("cast", []),
                "director": item.get("director", ""),
                "length": item.get("length", ""),
                "label": item.get("label", []),
                "link": item.get("link", ""),
                "preview": item.get("preview", ""),
                "preview_thumbs": item.get("preview_thumbs", []),
                "user_rating": item.get("user_rating", ""),
                "watched": item.get("watched", ""),
                "owned": item.get("owned", ""),
                "subscribed": item.get("subscribed", "")
            }
            # 如果有重复的，就不插入了
            if self.db.works.find_one({"link": document["link"]}):
                return

            # 插入文档到数据库
            self.db.works.insert_one(document)


class MySQLPipeline:
    """
    auth: mikeshinoda
    date: 2023.10.18
    """

    def __init__(self):
        self.items_dict = defaultdict(list)

    def open_spider(self, spider):
        # 连接到MySQL数据库
        self.connection = pymysql.connect(**db_config.get_mysql_config())
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"use {db_config.get_mysql_db_name()}")
        self.items_list = []

    def process_item(self, item, spider):
        try:
            print(item)
            self.cursor.execute("""
                   INSERT INTO works_table(link, preview, title, serial_number, release_date, length, 
                                               director, maker, label, user_rating, genres, cast, cast_id,
                                               subscribed, watched, owned, preview_thumbs) 
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                   ON DUPLICATE KEY UPDATE
                    link=VALUES(link), preview=VALUES(preview), title=VALUES(title), 
                    release_date=VALUES(release_date), length=VALUES(length), director=VALUES(director),
                    maker=VALUES(maker), label=VALUES(label), user_rating=VALUES(user_rating),
                    genres=VALUES(genres), cast=VALUES(cast), cast_id=VALUES(cast_id), subscribed=VALUES(subscribed),
                    watched=VALUES(watched), owned=VALUES(owned), preview_thumbs=VALUES(preview_thumbs);
               """, (
                item['link'],
                item['preview'],
                item['title'],
                item['serial_number'],
                item['release_date'],
                item['length'],
                item['director'],
                ", ".join(item['maker']),  # Assuming 'maker' is a list
                ", ".join(item['label']),  # Assuming 'label' is a list
                item['user_rating'],
                ", ".join(item['genres']),  # Assuming 'genres' is a list
                ", ".join(item['cast']),  # Assuming 'cast' is a list
                ", ".join(item['cast_id']),  # Assuming 'cast' is a list
                item['subscribed'],
                item['watched'],
                item['owned'],
                ", ".join(item['preview_thumbs'])
            ))
            self.connection.commit()
            return item
        except Exception as e:
            print(e)

    def close_spider(self, spider):
        """
        当spider关闭时执行的方法。
        该方法用于关闭数据库连接。
        """
        self.connection.close()
