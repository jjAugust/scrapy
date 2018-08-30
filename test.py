import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://traveldetail.fliggy.com/item.htm?spm=a1z10.3-b-s.w4011-15572466491.71.6eda23e8jznSyM&id=545656466491&rn=7a2ba7dec07c1a551097000421d1836b&abbucket=7',
    ]

    def parse(self, response):
            
            
        for quote in response.css('div.item-price'):
            yield {
                'text': quote.css('span::text').extract_first(),
#                 'author': quote.xpath('span/small/text()').extract_first(),
            }

        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)