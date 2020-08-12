# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

import scrapy
import sqlite3
import os
from bot.items import ChannelItem
from scrapy.pipelines.files import FilesPipeline

class BotPipeline:
    def process_item(self, item, spider):
        return item

class BotFilePipeline (FilesPipeline):
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['file_urls'])

    def file_path(self, request, response=None, info=None):
        path=super(BotFilePipeline, self).file_path(request,response,info)
        newPath = path.replace("full/","")
        return newPath

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        adapter = ItemAdapter(item)
        adapter['image_paths'] = image_paths[0]

        return item

class ChannleSqlitePipeline(object):

    def open_spider(self, spider):
        rootPath = os.path.abspath('.')
        dbFile = os.path.join(rootPath, 'config', 'data.set')

        self.conn = sqlite3.connect(dbFile)
        self.cur = self.conn.cursor()

    def close_spider(self, spider):
        self.conn.commit()
        self.conn.close()

    def process_item(self, item, spider):
        self.insert_db(item)
        return item

    def insert_db(self, item):
        values = (
            item['num'],
            item['title'],
            item['alias'],
            item['group'],
            '/static/' + item['image_paths'],
        )

        sql = 'INSERT INTO tvg_info ("num", "title", "alias", "group", "icon") VALUES (?,?,?,?,?)'
        self.cur.execute(sql, values)
