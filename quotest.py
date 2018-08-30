import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/tag/humor/',
    ]

    def parse(self, response):
        
#         for quote in response.css('div.quote'):
#             yield {
#                 'text': quote.css('span::text').extract_first(),
#                 'author': quote.css('small::text').extract_first(),
#             }
        yield {
            'test':response.css('span.tag-item').css('a::text').extract()
          }
    
        for o in response.css('span.tag-item'):
            yield{
               'fenkai':o.css('a::text').extract(),
            }
#         next_page = response.css('li.next a::attr("href")').extract_first()
#         if next_page is not None:
#             yield response.follow(next_page, self.parse)