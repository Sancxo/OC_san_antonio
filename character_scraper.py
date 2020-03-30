import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'characterspider'
    start_urls = [
        'https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Personnage_d%27animation_fran%C3%A7ais',
    ]

    def parse(self, response):
        for quote in response.css('div.mw-category div.mw-category-group  li'):
            yield {
                'character': quote.css('a ::text').get(),
            }
