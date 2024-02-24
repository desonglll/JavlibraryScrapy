import pymysql

import scrapyJAV.config.database_config as db_config
from scrapyJAV.config.arguments import get_config
from rich import print

dbname = get_config("mysql_db_name")


def is_existing(db_name):
    cursor = get_db_cursor()
    # 执行查询语句检查数据库是否存在
    cursor.execute("SHOW DATABASES LIKE %s", (db_name,))
    # 获取查询结果
    result = cursor.fetchone()
    # 如果结果不为空，说明数据库存在
    if result:
        return True
    else:
        return False


def get_db_cursor():
    connection = pymysql.connect(**db_config.get_mysql_config())
    cursor = connection.cursor()
    return cursor


def init_database():
    if is_existing(db_name=dbname):
        drop_database(db_name=dbname)
    create_database(db_name=dbname)
    cursor = get_db_cursor()
    sql = """CREATE TABLE IF NOT EXISTS `works_table` (
                `id` int NOT NULL AUTO_INCREMENT,
                `link` varchar(255) COLLATE utf8mb3_bin DEFAULT NULL,
                `preview` varchar(255) COLLATE utf8mb3_bin DEFAULT NULL,
                `title` varchar(255) COLLATE utf8mb3_bin DEFAULT NULL,
                `serial_number` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin NOT NULL UNIQUE,
                `release_date` varchar(255) COLLATE utf8mb3_bin DEFAULT NULL,
                `length` varchar(255) COLLATE utf8mb3_bin DEFAULT NULL,
                `director` varchar(255) COLLATE utf8mb3_bin DEFAULT NULL,
                `maker` varchar(255) COLLATE utf8mb3_bin DEFAULT NULL,
                `label` varchar(255) COLLATE utf8mb3_bin DEFAULT NULL,
                `user_rating` varchar(255) COLLATE utf8mb3_bin DEFAULT NULL,
                `genres` varchar(255) COLLATE utf8mb3_bin DEFAULT NULL,
                `cast` varchar(255) COLLATE utf8mb3_bin DEFAULT NULL,
                `cast_id` varchar(255) COLLATE utf8mb3_bin DEFAULT NULL,
                `subscribed` varchar(255) COLLATE utf8mb3_bin DEFAULT NULL,
                `watched` varchar(255) COLLATE utf8mb3_bin DEFAULT NULL,
                `owned` varchar(255) COLLATE utf8mb3_bin DEFAULT NULL,
                `preview_thumbs` longtext COLLATE utf8mb3_bin DEFAULT NULL,
                PRIMARY KEY (`id`,`serial_number`) USING BTREE
              ) ENGINE=InnoDB AUTO_INCREMENT=10613 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;"""

    print(sql)
    cursor.execute(f"use {db_config.get_mysql_db_name()}")
    cursor.execute(sql)
    pass


def drop_database(db_name):
    """
    Drops the specified database if it exists.

    Args:
        db_name (str): Name of the database.

    Returns:
        None
    """
    if is_existing(db_name=db_name):
        cursor = get_db_cursor()
        try:
            cursor.execute(f"DROP DATABASE IF EXISTS {db_name}")
            print(f"Database '{db_name}' dropped successfully.")
        except Exception as e:
            print(f"Error dropping database '{db_name}': {e}")
        finally:
            cursor.close()
    else:
        print(f'''[bold red]Database '{db_name}' does not exist.[/bold red]''')
        pass


def create_database(db_name):
    """
    Creates a new database if it doesn't already exist.

    Args:
        db_name (str): Name of the database.

    Returns:
        None
    """
    # 检查数据库是否存在
    cursor = get_db_cursor()
    db_exists = cursor.execute("SHOW DATABASES LIKE %s", db_name)
    if not db_exists:
        # 如果数据库不存在，则创建数据库
        cursor.execute(f"CREATE DATABASE {db_name};")
        print(f"[bold green]Creating {db_name} successfully![/bold green]")
    else:
        print(f"[bold red]Database: {db_name} already exists![/bold red]")
