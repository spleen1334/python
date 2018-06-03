# -*- coding: utf-8 -*-
import scrapy
from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class BooksSpider(CrawlSpider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    # LinkExtractor automaticly follows links and extracts pages
    # deny_domains - skip links
    # allow = only focus on links which container string
    rules = (Rule(LinkExtractor(allow=('music'), deny_domains=('google.com')), callback='parse_page', follow=True),)

    def parse_page(self, response):
        page = response.url.split("/")[-2]
        filename = 'books-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
