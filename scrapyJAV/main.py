# -*- coding: utf-8 -*-
"""
File: main
Description: 
Author: mikeshinoda
Date: 2024/1/19
"""
import getopt
import sys

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

import dbop.mysql_op as mysql_op
from scrapyJAV.config.arguments import get_config
from scrapyJAV.spiders.works_spider import WorksSpider
from rich import print as rprint

from tools.guide_info import print_all


# TODO: Add your code here
def main():
    if not mysql_op.is_existing(get_config("mysql_db_name")):
        mysql_op.init_database()
    # 创建一个CrawlerProcess
    process = CrawlerProcess(get_project_settings())
    # 先启动WorksSpider
    process.crawl(WorksSpider)
    # process.crawl(WorksListSpider)
    process.start()


def guide():
    opts, args = getopt.getopt(sys.argv[1:], "d:c:", ['database_operation', 'crawl'])  # Syntax error corrected here
    for opt, arg in opts:
        if opt == '-d':
            if arg == "delete":
                rprint(f"[bold green]Deleting database: {get_config('mysql_db_name')}[/bold green]!")
                mysql_op.drop_database(get_config("mysql_db_name"))
            if arg == "init":
                rprint(f"[bold green]Initializing database: {get_config('mysql_db_name')}[/bold green]!")
                mysql_op.init_database()
        if opt == '-c':
            if arg == "start":
                main()
        else:
            print_all()


if __name__ == "__main__":
    guide()
    pass
