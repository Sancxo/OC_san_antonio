import scrapy
from scrapy.selector import Selector


class QuotesSpider(scrapy.Spider):
    name = 'quotespider'
    start_urls = [
        'https://www.babelio.com/auteur/Frederic-Dard/7187/citations'
    ]

    def parse(self, response):
        for quote in response.css('div.post_con div.text.row div'):
            yield {
                'quote': quote.css('div ::text').get(),
            }
