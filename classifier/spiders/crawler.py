# -*- coding: utf-8 -*-
import scrapy
import newspaper

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.item import Item, Field

class CrawlerSpider(CrawlSpider):
    name = 'crawler'
    #allowed_domains = ['twitter.com']
    start_urls = ['http://www.twitter.com']
    
    rules = (Rule(LinkExtractor(), callback='parse_item', follow=True), )

    def parse_item(self, response):
        item = Field()
        item['url'] = response.url
        return item