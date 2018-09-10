import scrapy
from taobao.items import TaobaoItem
from taobao.emailSender import emailSender  # 导入发信模块
import datetime



##有重定向问题，需要解决登陆问题
class QuotesSpider(scrapy.Spider):
    def __init__(self, wantprice=None, url=None, para1=None, para0=None, para2=None, para3=None, para4=None):
        if wantprice is None:
            self.wantprice = 0
        else:
            self.wantprice=wantprice
        if para1 is None:
            self.para1 = "7"
            self.para0 = "0"
            self.para2 = "0"
            self.para3 = "0"
            self.para4 = "0"
        else:
            self.para1=int(para1)-1
            self.para0=int(para0)-1
            self.para2=para2
            self.para3=para3
            self.para4=para4
            
        if url is None:
            self.url = ''
            self.start_urls=self.url
        else:
            self.start_urls=url  
        
    name = "taobao"
    

    def start_requests(self):
        #启动报告
#         emailSenderClient = emailSender()
#         toSendEmailLst = ['junjie.sop@gmail.com', 'junjie19890815@126.com']
#         startTime = datetime.datetime.now()
#         subject = "爬虫启动状态汇报：name = taobao, startTime = "+str(startTime)
#         body = "细节：start successs! at:"+str(startTime)
#         emailSenderClient.sendEmail(toSendEmailLst, subject, body)  # 发送邮件

        yield scrapy.Request(self.start_urls,meta={'para0': self.para0,'para1': self.para1,'para2': self.para2,'para3': self.para3,'para4': self.para4},callback=self.parse_news)
        
#         for eachUrl in self.start_urls:
#             yield scrapy.Request(eachUrl,callback=self.parse_news)
            
    def parse_news(self, response):

        t=TaobaoItem()
        price=response.xpath('.//dd[@class="price-content big-price"]/span/text()').extract_first()
        t['price']=price
        if round(float(price))<round(float(self.wantprice)):
            emailSenderClient = emailSender()
            toSendEmailLst = ['junjie.sop@gmail.com', 'junjie19890815@126.com']
            startTime = datetime.datetime.now()
            subject = "低价提醒"
            body = "细节：检测到有低于您设置的低价"
            emailSenderClient.sendEmail(toSendEmailLst, subject, body)  # 发送邮件
        yield t