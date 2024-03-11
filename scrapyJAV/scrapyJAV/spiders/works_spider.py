# -*- coding: utf-8 -*-
"""
File: works_spider
Description: 
Author: mikeshinoda
Date: 2024/1/19
"""
# TODO: Add your code here
from typing import Any
from urllib.parse import urljoin
import scrapy
from scrapy.http import Response
from scrapyJAV.config.arguments import get_config
from scrapyJAV.items import WorksItem


class WorksSpider(scrapy.Spider):
    name = 'works_sp'
    base_url_template = (
        "{url}/vl_star.php?list&mode=2&s={actor_id}&page={page}"
    )
    items_dict = {}

    custom_settings = {
        'ITEM_PIPELINES': {
            'scrapyJAV.pipelines.MySQLPipeline': 1,
            # 'scrapyJAV.pipelines.MongoDBPipeline': 2,
        },
    }

    def start_requests(self):
        actor_ids = get_config("ids")
        cookies = {
            'over18': '18',
        }
        for actor_id in actor_ids:
            yield scrapy.Request(
                url=self.base_url_template.format(url=get_config("base_url"), actor_id=actor_id, page=1),
                callback=self.parse_pagination,
                cookies=cookies,
                dont_filter=True,  # 即使是重复请求也继续执行
                meta={
                    "base_url": self.base_url_template.format(
                        url=get_config("base_url"), actor_id=actor_id, page="{}"
                    ),
                    "cast_id": actor_id
                },
            )
            # 发送一个额外的请求以爬取第一页的数据
            # yield scrapy.Request(
            #     url=self.base_url_template.format(url=get_config("base_url"), actor_id=actor_id, page=1),
            #     callback=self.parse,
            #     dont_filter=True,  # 即使是重复请求也继续执行
            #     meta={
            #         "cast_id": actor_id
            #     })

    def parse_pagination(self, response):
        base_url = response.meta["base_url"]
        cast_id = response.meta["cast_id"]
        # 解析最后一页的数字
        last_page = response.xpath('//a[@class="page last"]/@href').re(r"page=(\d+)")
        last_page_num = int(last_page[0] if last_page else 1)
        # 使用for循环生成每一页的URL，并使用parse方法爬取数据
        custom_page = get_config("custom_page")
        for page in range(1, last_page_num + 1 if custom_page == -1 else custom_page + 1):
            yield scrapy.Request(url=base_url.format(page), callback=self.parse, meta={
                "cast_id": cast_id
            })

    def parse(self, response: Response, **kwargs: Any) -> Any:
        cast_id = response.meta["cast_id"]
        for row in response.xpath(
                '//table[@class="videotextlist"]/tr[not(contains(@class, "header"))]'
        ):
            # 生成每个作品的链接
            link = row.xpath('.//td[@class="title"]/div[@class="video"]/a/@href').get()
            absolute_link = response.urljoin(link)
            yield scrapy.Request(
                url=absolute_link,
                callback=self.parse_work,
                meta={
                    "cast_id": cast_id
                }
            )

    def parse_work(self, response):
        cast_id = response.meta["cast_id"]
        item = WorksItem()
        item["link"] = urljoin("https://www.javlibrary.com/", response.css("#video_title").css("a::attr(href)").get())
        item["preview"] = response.css("#video_jacket").css("img::attr(src)").get(default="")
        item["title"] = response.css("#video_title").css("a::text").get(default="")
        item["serial_number"] = response.css("#video_id").css("td.text::text").get(default="")
        item["release_date"] = response.css("#video_date").css("td.text::text").get(default="")
        item["length"] = response.css("#video_length").css("span.text::text").get(default="")
        item["director"] = response.css("#video_director").css("td.text::text").get(default="")
        item["maker"] = response.css("#video_maker").css("span.maker").css("a::text").getall()
        item["label"] = response.css("#video_label").css("td.text").css("span.label").css("a::text").getall()
        item["user_rating"] = response.css("#video_review").css("td.text").css("span.score::text").get(default="")
        item["genres"] = response.css("#video_genres").css("td.text").css("span.genre").css("a::text").getall()
        item["cast"] = response.css("#video_cast").css("td.text").css("span.star").css("a::text").getall()
        item["cast_id"] = cast_id,
        item["subscribed"] = response.css("#video_favorite_edit").css("#subscribed").css("a::text").get(default="")
        item["watched"] = response.css("#video_favorite_edit").css("#watched").css("a::text").get(default="")
        item["owned"] = response.css("#video_favorite_edit").css("#owned").css("a::text").get(default="")
        item["preview_thumbs"] = response.css('.previewthumbs a:not([href="#"])::attr(href)').extract()
        yield item
