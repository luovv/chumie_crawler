# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
# from scrapy.contrib.exporter import JsonItemExporter
from pymongo import MongoClient

class JsonWriterPipeline(object):

    def open_spider(self, spider):
        # self.db = MongoClient('mongodb://35.161.12.150/myapp', 27017).myapp.webcontents
        self.db = MongoClient('mongodb://localhost/myapp', 27017).myapp.webcontents

    def close_spider(self, spider):
        pass
        # 默认是unicode，ensure_ascii=False存中文
        # indent=4就是带缩进的，默认是不换行的
        # line = json.dumps(self.itemList, ensure_ascii=False, indent=4) + "\n"
        #
        # file = open('items.json', 'w', encoding='utf-8')
        # file.write(line)
        # file.close()

    def process_item(self, item, spider):
        try:
            self.db.insert_one(item)
        except:
            print('duplicate')
        return item