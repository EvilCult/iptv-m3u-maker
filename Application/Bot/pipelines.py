# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy, sqlite3, time, os, sys

from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from Bot.items import ChannelItem
from scrapy.pipelines.files import FilesPipeline

class BotPipeline:
    def process_item(self, item, spider):
        return item

class BotFilePipeline (FilesPipeline):
    def get_media_requests(self, item, info):
        if item['file_urls'] != '':
            yield scrapy.Request(item['file_urls'])

    def file_path(self, request, response=None, info=None):
        path=super(BotFilePipeline, self).file_path(request,response,info)
        newPath = path.replace("full/","")
        return newPath

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]

        adapter = ItemAdapter(item)
        if not image_paths:
            adapter['image_paths'] = ''
        else :
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
        self.savData(item)
        return item

    def savData(self, item):
        now = int(time.time())

        try:
            if item['image_paths'] != '' :
                imgPath = '/static/' + item['image_paths']
            else :
                imgPath = ''
            values = (
                item['num'],
                item['title'],
                item['alias'],
                item['group'],
                imgPath,
                now
            )
            sql = (
                'INSERT OR IGNORE INTO tvg_info '
                '("num", "title", "alias", "group", "icon", udtime)'
                ' VALUES '
                '(?, ?, ?, ?, ?, ?);'
            )
            self.cur.execute(sql, values)

            values = (
                item['num'],
                item['title'],
                item['group'],
                imgPath,
                now,
                item['alias']
            )
            sql = (
                'UPDATE tvg_info SET'
                ' "num" = ?, "title" = ?, "group" = ?, "icon" = ?, "udtime" = ?'
                ' WHERE "alias" = ?;'
            )
            self.cur.execute(sql, values)

            logStr = 'Update: [Channel] - %s' % (item['title'])
            self.addLog('info', logStr)
        except:
            self.addLog('err', sys.exc_info()[0])

    def addLog(self, typ, data):
        sql = (
            'INSERT INTO "log" '
            '("typ", "msg", "udtime") '
            'VALUES (?, ?, ?)'
        )

        values = (
            typ,
            data,
            int(time.time())
        )

        self.cur.execute(sql, values)
