# -*- coding: utf-8 -*-
import scrapy
import newspaper
from newspaper import Article

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.item import Item, Field
from datetime import datetime

class CrawlerSpider(CrawlSpider):
    name = 'crawler'
    #allowed_domains = ['twitter.com']
    start_urls = ['http://www.twitter.com']
    
    rules = (Rule(LinkExtractor(), callback='parse_item', follow=True), )

    def parse_item(self, response):
        item = Field()
        item['url'] = response.url
        article = Article(response.url)
        article.download()
        article.parse()
        self.logger.info('URL: ' + response.url)

        file = open("logs/extractions.log", "a")
        file.write("\n\n[URL]\n")
        file.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        file.write("\n") 
        file.write(response.url)
        file.write("\n") 
        file.write(article.text)  
        file.close() 

        return item