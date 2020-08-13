import scrapy

from Bot.items import ChannelItem

class ChannelSpider(scrapy.Spider):
    name = 'channel'
    allowed_domains = ['51zmt.top']
    start_urls = ['http://epg.51zmt.top:8000/']

    def parse(self, response):
        sel = scrapy.Selector(response)

        channels = sel.xpath('/html/body/div/table/tbody/tr')
        channels = channels[1:]
        channels = channels[0:10]

        for channel in channels:
            item = ChannelItem()

            item['num'] = channel.xpath('th/text()').extract_first()
            item['title'] = channel.xpath('td[2]/text()').extract_first().lower()
            item['alias'] = channel.xpath('td[3]/text()').extract_first().lower()
            item['group'] = channel.xpath('td[4]/text()').extract_first().lower()
            item['file_urls'] = channel.xpath('td[1]/a/@href').extract_first()

            yield item
