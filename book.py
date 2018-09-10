# -*- coding: utf-8 -*-
import scrapy
import BookItem
 
class NovelSpider(scrapy.Spider):
    name = 'novel'
    ITEM_PIPELINES = {
        'myproject.pipelines.ReadnovelPipeline': 300,
        'myproject.pipelines.JsonWriterPipeline': 800,
    }
    custom_settings = {
        'FEED_EXPORT_ENCODING' : 'utf-8',
    }
    allowed_domains = ['readnovel.com']
    start_urls = ['https://www.readnovel.com/free/all']
 
    def parse(self, response):
 
        divs = response.xpath('//div[@class="book-info"]')
 
        for div in divs:
            # 小说名称
            name = div.xpath('h3/a/text()').extract_first('')
            # 小说作者
            author = div.xpath('h4/a/text()').extract_first('')
            # 小说类型
            novel_type = div.xpath('p/span[@class="org"]/text()').extract_first('')
            # 小说状态
            status = div.xpath('p/span[@class="red"]/text()').extract_first('')
            # 小说字数
            numbers = div.xpath('p/span[@class="blue"]/text()').extract_first('')
            # 创建item
            item = BookItem()
            item['name'] = name
            item['author'] = author
            item['novel_type'] = novel_type
            item['status'] = status
            item['numbers'] = numbers
            # 交给pipeline处理
            yield item
 
