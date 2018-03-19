# -*- coding: utf-8 -*-
import scrapy
import newspaper
from newspaper import Article

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.item import Item, Field
from datetime import datetime

class GoogleNewsSpider(CrawlSpider):
    name = 'google.news'
    start_urls = ['https://news.google.com/news/']

    rules = (Rule(LinkExtractor(), callback='parse_item', follow=True), )

    def parse_item(self, response):
        item = Field()
        item['url'] = response.url
        article = Article(response.url)
        article.download()
        article.parse()
        self.logger.info('URL: ' + response.url)

        return item
