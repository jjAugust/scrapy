
from wxnews.items import WxnewsItem


class WxnewsSpider(scrapy.Spider):
    name = 'wxnews'
    start_urls = [
        'http://weixin.sogou.com'
    ]

    def parse(self, response):
        news_href_list=response.xpath('//ul[@class="news-list"]/li/div[2]/h3/a/@href')
        #print response.url
        for href in news_href_list:
            url=response.urljoin(href.extract())
            yield scrapy.Request(url,callback=self.parse_news)


    def parse_news(self, response):
        title=response.xpath('.//div[@id="page-content"]/div/h2/text()').extract_first()
        time=response.xpath('.//div[@id="page-content"]/div/div[1]/em[1]/text()').extract_first()
        post_user=response.xpath('.//a[@id="post-user"]/text()').extract_first()

        #print title.strip()
        #print time.strip()
        #print post_user.strip()

        #print " "

        #yield {'title':title,
        #      'time':time,
        #     'post_user':post_user
        # }


        news=WxnewsItem()
        news['title']=title.strip()
        news['time']=time
        news['post_user']=post_user

        yield news

from selenium import webdriver
from scrapy.http import HtmlResponse
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from random import choice

class SeleniumMiddleware(object):
    def process_request(self, request, spider):
        click_page_url="http://weixin.sogou.com"
        if request.url==click_page_url:
            driver = webdriver.PhantomJS()
            try:
                driver.get(request.url)
                driver.implicitly_wait(3)
                time.sleep(5)

                look_more=".//div[@class='jzgd']/a"
                for n in range(4):
                    driver.find_element_by_xpath(look_more).click()  # 数据由js来控制,点击后加载数据
                    time.sleep(5)

                true_page = driver.page_source
                driver.close()

                return HtmlResponse(request.url,body = true_page,encoding = 'utf-8',request = request,)

            except:
                print("get news data failed")
        else:
            return None