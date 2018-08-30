# -*- coding: utf-8 -*-
 
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
import os
class ReadnovelPipeline(object):
    def process_item(self, item, spider):
        return item
 
# 定义一个写入json数据的pipeline
class JSONWriterPipeline(object):
 
    def __init__(self):
        # 打开文件,做写入前的准备
        self.file = codecs.open('quotes.json','w+',encoding='utf-8')
        # 先写入[
        self.file.write('[')
 
    # 处理item的函数
    def process_item(self, item, spider):
        # 1.把item转换字典类型
        item = dict(item)
        # 2.把字典对象转换为json字符串
        # json.loads() 将json字符串转换python
        # json.dumps() 将python对象转换json字符串
        json_str = json.dumps(item,ensure_ascii=False)
        self.file.write(json_str)
        # 写入,逗号 把每个字典分开
        self.file.write(',')
        # 返回一个item 交给下一个pipeline处理
        return item
 
    # 爬虫关闭时,将文件填写完整,关闭文件
    def close_spider(self,spider):
        # 将光标移到文件末尾字符之前
        # offset偏移量  whence
        # 0文件起始位置  1当前位置  2文件末尾
        # SEEK_END 文件末尾
        # SEEK_SET 文件开始
        # SEEK_CUR 当前位置
        self.file.seek(-1,os.SEEK_END)
        # 删除文件末尾最后一个字符
        # truncate() 不填参数,表示从当前的位置截取,当前位置之后的数据都不要
        self.file.truncate()
        # 写入右括号
        self.file.write(']')
        # 关闭文件
        self.file.close()
 
