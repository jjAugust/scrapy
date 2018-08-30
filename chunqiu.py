import scrapy
import time
import base64
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from buluo.items import BuluoItem

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    custom_settings = {
        'FEED_EXPORT_ENCODING' : 'utf-8',
    }
    start_urls = [
        'https://china-sss.fliggy.com/category-283146094-1518913137.htm?spm=a1z10.1-b-s.w5002-15573120513.101.3cd65e45Iu2mfX&search=y&catName=%C8%D5%B1%BE',
    ]

    def parse(self, response):
        
#         for quote in response.css('div.quote'):
#             yield {
#                 'text': quote.css('span::text').extract_first(),
#                 'author': quote.css('small::text').extract_first(),
#             }
#         yield {
#             'test':response.css('div.item5line1').css('a::text').extract()
#           }
    
        for o in response.css('dd.detail'):
            yield{
                'title':o.css('a::text').extract(),
                'price':o.css('span.c-price::text').extract(),
            }
#         next_page = response.css('li.next a::attr("href")').extract_first()
#         if next_page is not None:
#             yield response.follow(next_page, self.parse)