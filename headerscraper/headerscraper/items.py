# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

# import scrapy // import scrapy is giving me some errors from pylance!

class HeaderscraperItem(scrapy.Item):
    name = 'dollarspider'
    allowed_domains = ['cryptonews.com']
    start_urls = ['https://cryptonews.com/']
    pass
