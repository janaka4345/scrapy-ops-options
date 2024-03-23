import scrapy


class PlaywriteSpider(scrapy.Spider):
    name = "playwrite"
    allowed_domains = ["example.com"]
    start_urls = ["https://example.com"]

    def parse(self, response):
        pass
