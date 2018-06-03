# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser

from quotes_spider.items import QuotesSpiderItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    # allowed_domains = ['quotes.toscrape.com']
    # start_urls = ['http://quotes.toscrape.com/']
    start_urls = ['http://quotes.toscrape.com/login']

    def parse(self, response):
        """
        First login and then scrape homepage
        """
        token = response.xpath(
            '//*[@name="csrf_token"]/@value').extract_first()
        return FormRequest.from_response(response,
                                         formdata={'csrf_token': token,
                                                   'password': 'foobar',
                                                   'username': 'foobar'},
                                         callback=self.home_page_advanced)
    def list_items(self, response):
        """
        Scrape authors/text/tags from all 10 pages
        Command for output to csv:
            scrapy crawl quotes -o filename.csv
        """
        quotes = response.xpath('//*[@class="quote"]')
        for quote in quotes:
            text = quote.xpath('.//*[@class="text"]/text()').extract_first()
            author = quote.xpath('.//*[@itemprop="author"]/text()').extract_first()
            tags = quote.xpath('.//*[@itemprop="keywords"]/@content').extract_first()

            # CONSOLE OUTPUT
            # print('\n')
            # print(text)
            # print(author)
            # print(tags)

            yield{'Text': text,
                  'Author': author,
                  'Tags': tags}

        next_page_url = response.xpath('//*[@class="next"]/a/@href').extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)
        yield scrapy.Request(absolute_next_page_url, callback=self.parse)

    def home_page_advanced(self, response):
        """
        Scrape homepage with help of pipelines.py & items.py
        """
        # open_in_browser(response)
        l = ItemLoader(item=QuotesSpiderItem(), response=response)

        h1_tag = response.xpath('//h1/a/text()').extract_first()
        tags = response.xpath('//*[@class="tag-item"]/a/text()').extract()

        l.add_value('h1_tag', h1_tag)
        l.add_value('tags', tags)

        return l.load_item()

