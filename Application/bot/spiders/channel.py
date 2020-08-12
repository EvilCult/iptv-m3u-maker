import scrapy


class ChannelSpider(scrapy.Spider):
    name = 'channel'
    allowed_domains = ['51zmt.top']
    start_urls = ['http://51zmt.top/']

    def parse(self, response):
        pass
