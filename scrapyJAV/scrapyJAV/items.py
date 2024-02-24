# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WorksItem(scrapy.Item):
    link = scrapy.Field()
    preview = scrapy.Field()
    #
    title = scrapy.Field()
    serial_number = scrapy.Field()
    release_date = scrapy.Field()
    length = scrapy.Field()
    director = scrapy.Field()
    maker = scrapy.Field()
    label = scrapy.Field()
    user_rating = scrapy.Field()
    genres = scrapy.Field()
    cast = scrapy.Field()
    cast_id = scrapy.Field()
    #
    subscribed = scrapy.Field()
    watched = scrapy.Field()
    owned = scrapy.Field()
    preview_thumbs = scrapy.Field()


class ScrapyjavItem(scrapy.Item):
    pass
