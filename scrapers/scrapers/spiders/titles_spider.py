import scrapy

class TitlesSpider(scrapy.Spider):
    name = 'titles'
    start_urls = [
        'https://cryptonews.com/news/bitcoin-news',
    ]    

    def parse(self, response):
        for article in response.css('article.article-item'):
            yield {
                "title": article.css('a.article__title::text').get(),
                "datetime": article.css('div.article__badge').css('div.article__badge-date::attr(data-utctime)').get(),
            }
        