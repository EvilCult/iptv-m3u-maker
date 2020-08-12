# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import scrapy
from bot.items import Channeltem
from scrapy.pipelines.images import ImagesPipeline

class BotPipeline:
    def process_item(self, item, spider):
        return item

class BotImgPipeline (ImagesPipeline):
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['image_urls'])

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        adapter = ItemAdapter(item)
        adapter['image_paths'] = image_paths

        return item
