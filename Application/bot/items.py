# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BotItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ChannelItem(scrapy.Item):
    title       = scrapy.Field()
    alias       = scrapy.Field()
    group        = scrapy.Field()
    image_urls  = scrapy.Field()
    images      = scrapy.Field()
    image_paths = scrapy.Field()
