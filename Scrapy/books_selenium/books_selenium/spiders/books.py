# -*- coding: utf-8 -*-
from time import sleep

from scrapy import Spider
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.http import Request
from selenium.common.exceptions import NoSuchElementException


class BooksSpider(Spider):
    """
    Scraping web sites using Selenium
    """
    name = 'books'
    allowed_domains = ['books.toscrape.com']

    def start_requests(self):
        self.driver = webdriver.Chrome('/Users/spleen/Programming/Python/Scrapy/books_selenium/chromedriver')
        self.driver.get('http://books.toscrape.com')

        # First page on load
        self.select_books()

        while True:
            try:
                next_page = self.driver.find_element_by_xpath('//a[text()="next"]')
                sleep(3)
                self.logger.info('Sleeping for 3 seconds.')
                next_page.click()

                # Every other page
                self.select_books()

            except NoSuchElementException:
                self.logger.info('No more pages to load.')
                self.driver.quit()
                break

    def parse_book(self, response):
        title = response.css('h1::text').extract_first()
        url = response.request.url
        yield {'title': title, 'url':url}


    def select_books(self):
        sel = Selector(text=self.driver.page_source)
        books = sel.xpath('//h3/a/@href').extract()
        for book in books:

            url = 'http://books.toscrape.com/' + book
            yield Request(url, callback=self.parse_book)