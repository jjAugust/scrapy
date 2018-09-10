import scrapy
from JD.items import JdItem
from JD.emailSender import emailSender  # 导入发信模块
import datetime



##有重定向问题，需要解决登陆问题
class QuotesSpider(scrapy.Spider):
    def __init__(self, wantprice=None, JDType1=None,JDType2=None,JDType3=None,JDType4=None, url=None, email=None):
        if wantprice is None:
            self.wantprice = 0
        else:
            self.wantprice=wantprice
            
        if email is None:
            self.email = "junjie19890815@126.com"
        else:
            self.email = email
            
        if url is None:
            self.url = ''
            self.start_urls=self.url
        else:
            self.start_urls=url 
            
        if JDType1 is None:
            JDType1 = 1
            JDType2 = 1
            JDType3 = 1
            JDType4 = 1
        else:
            self.JDType1 = JDType1
            self.JDType2 = JDType2
            self.JDType3 = JDType3
            self.JDType4 = JDType4
        
    name = "JD"
    

    def start_requests(self):
        yield scrapy.Request(self.start_urls,meta={'JDType1':self.JDType1,'JDType2':self.JDType2,'JDType3':self.JDType3,'JDType4':self.JDType4},callback=self.parse_news)
        
            
    def parse_news(self, response):

        t=JdItem()
        price=response.xpath('.//span[@class="p-price"]/span[2]/text()').extract_first()
        t['price']=price
        info=response.xpath('.//div[@class="sku-name"]/text()').extract_first()
        t['info']=info.strip()
        time = datetime.datetime.now()
        t['time'] = time
        try:
            if(round(float(price))<round(float(self.wantprice))):
            
                emailSenderClient = emailSender()
                toSendEmailLst = [self.email]
                startTime = datetime.datetime.now()
                subject = "低价提醒"+info.strip()
                body = "细节：检测到有低于您设置的低价"
                emailSenderClient.sendEmail(toSendEmailLst, subject, body)  # 发送邮件
        except exception:
            pass
               
        yield t