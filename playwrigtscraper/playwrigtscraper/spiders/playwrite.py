import scrapy


class PlaywriteSpider(scrapy.Spider):
    name = "playwrite"

    def start_requests(self):
        rurl = "https://quotes.toscrape.com/js/"
        yield scrapy.Request(url=rurl, meta={'playwright': True})

    def parse(self, response):
        quote_items=response.css('div.quote')
        for quote in quote_items:
            yield{   
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }
