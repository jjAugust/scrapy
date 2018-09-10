# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

from JD.items import JdItem

class JDPipeline(object):
    def __init__(self):
        clinet = pymongo.MongoClient("localhost", 27017)
        db = clinet["JD"]
        self.JDItem = db["JDItem"]
        
    def process_item(self, item, spider):
        try:
            self.JDItem.insert(dict(item))
        except Exception:
            pass
        return item