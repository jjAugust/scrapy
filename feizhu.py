import scrapy

##有重定向问题，需要解决登陆问题
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://tripcart.fliggy.com/cartList.htm',
    ]

    def parse(self, response):
            
            
        for quote in response.css('ul.product-list J_product-list'):
            yield {
                'text': quote.css('span.J_total_price::text').extract_first(),
            }

        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)