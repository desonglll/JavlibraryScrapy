from scrapyJAV.config.arguments import get_config


def get_mysql_config():
    """
    获取Mysql服务器的配置参数。

    Returns:
        dict: 包含Mysql服务器配置参数的字典。
    """
    mysql_config = get_config("mysql_config")
    return mysql_config


def get_mysql_db_name():
    return get_config("mysql_db_name")


if __name__ == "__main__":
    # 调用重新创建表的函数
    pass
