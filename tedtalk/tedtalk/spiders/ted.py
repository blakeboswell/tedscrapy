# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from tedtalk.items import TedtalkItem


class TedSpider(CrawlSpider):
    name = 'ted'
    allowed_domains = ['www.ted.com']
    start_urls = ['https://www.ted.com/talks/']

    rules = [
        Rule(
             LinkExtractor(allow=['/talks\\?page=\d+']),
             callback='request_talkpage',
             follow=True
        )
    ]

    def request_talkpage(self, response):
        print response.url

    # def parse_talkpage(self, response):
    #     sel_list = response.xpath()
    #     for sel in sel_list:
    #         item = TedTalkItem()
    #         item['speaker'] = sel.xpath('//h4[@class="h12 talk-link__speaker"]/text()')
    #         item['title'] = sel.xpath('//h4[@class="h9 m5"]//a/text()')
    #         item['url'] = sel.xpath('//h4[@class="h9 m5"]//a/@href')
    #         item['meta'] = sel.xpath('//div[@class="meta"]//span[@class="meta__val"]//text()')
