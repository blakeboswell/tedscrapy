# -*- coding: utf-8 -*-
from scrapy.http import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tedtalk.items import TedtalkItem, XPATHS


class TedSpider(CrawlSpider):
    ''' scrape the ted talk page
    '''
    name = 'ted'
    allowed_domains = ['ted.com']
    start_urls = ['http://www.ted.com/talks/']

    rules = (
        Rule(LinkExtractor(allow=r'talks\?page=\d+'),
             follow=True),
        Rule(LinkExtractor(allow=r'talks\/[a-z_]+'),
             follow=True,
             callback='parse_page')
    )

    def parse_page(self, response):
        hxs = response.selector
        meta = {
            'speaker': hxs.xpath(XPATHS['speaker']).extract(),
            'title': hxs.xpath(XPATHS['title']).extract(),
            'viewn': hxs.xpath(XPATHS['viewn']).extract()
        }
        newurl = '%s/transcript?language=en' % response.url
        yield Request(newurl, callback=self.parse_transcript, meta=meta)

    def parse_transcript(self, response):
        item = TedtalkItem()
        hxs = response.selector

        transcript = hxs.xpath(XPATHS['transcript']).extract()
        transcript = ' '.join([t.strip() for t in transcript if t != '\n'])

        item['speaker'] = response.meta['speaker']
        item['title'] = response.meta['title']
        item['speaker'] = response.meta['speaker']
        item['transcript'] = transcript

        return item
