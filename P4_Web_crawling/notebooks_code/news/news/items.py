import scrapy


class NewsItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
