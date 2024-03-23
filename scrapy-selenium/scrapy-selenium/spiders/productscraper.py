from typing import Iterable
import scrapy
from scrapy_selenium import SeleniumRequest


class ProductscraperSpider(scrapy.Spider):
    name = "productscraper"
    # allowed_domains = ["example.com"]
    # start_urls = ["https://example.com"]
    
    def start_requests(self):
            url = 'https://quotes.toscrape.com/js/'
            yield SeleniumRequest(url=url, callback=self.parse)


    def parse(self, response):
        quote_items=response.css('div.quote')
        for quote in quote_items:
            yield{   
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                # 'tags': quote.css('div.tags a.tag::text').getall(),
            }
			
