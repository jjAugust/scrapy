# -*- coding:utf-8 -*-
import scrapy
from wxnews.items import WxnewsItem


class WxnewsSpider(scrapy.Spider):
    name = 'wxnews'
    start_urls = [
        'http://weixin.sogou.com'
    ]
    def parse(self, response):
        news_href_list=response.xpath('//ul[@class="news-list"]/li')
        for href in news_href_list:
            title=href.xpath('.//div[2]/h3/a/text()').extract_first()
            news=WxnewsItem()
            news['title']=title
            yield news


    
#     def parse(self, response):
#         news_href_list=response.xpath('//ul[@class="news-list"]/li/div[2]/h3/a/@href')
#         #print response.url
#         for href in news_href_list:
#             url=response.urljoin(href.extract())
#             yield scrapy.Request(url,callback=self.parse_news)


#     def parse_news(self, response):
# #         title=response.xpath('.//div[@id="page-content"]/div/div/h2/text()').extract_first()
#         title=response.xpath('.//h2[@id="activity-name"]/text()').extract_first()
#         time=response.xpath('.//em[@id="publish_time"]/text()').extract_first()
#         post_user=response.xpath('.//a[@id="js_name"]/text()').extract_first()

#         #print title.strip()
#         #print time.strip()
#         #print post_user.strip()

#         #print " "

#         #yield {'title':title,
#         #      'time':time,
#         #     'post_user':post_user
#         # }


#         news=WxnewsItem()
#         news['title']=title.strip()
#         news['time']=time
#         news['post_user']=post_user.strip()

#         yield news