# -*- coding: utf-8 -*-
from scrapy.http import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tedtalk.items import TedtalkItem, XPATHS


class TedSpider(CrawlSpider):
    ''' scrape transcripts and meta info from TED talk page
    '''
    name = 'ted'
    allowed_domains = ['ted.com']
    start_urls = ['http://www.ted.com/talks/']

    pagexp = r'//a[@class="pagination__item pagination__link"]'
    talkxp = r'//div[@class="media__image media__image--thumb talk-link__image"]'

    rules = (
        Rule(LinkExtractor(allow=r'talks\?page=\d+',
                           restrict_xpaths=pagexp),
             follow=True),
        Rule(LinkExtractor(allow=r'talks\/[a-z_]+',
                           restrict_xpaths=talkxp),
             follow=True,
             callback='parse_page')
    )

    def parse_page(self, response):
        ''' extract information from TED talk page, follow transcript url
        '''
        hxs = response.selector
        meta = {
            'speaker': hxs.xpath(XPATHS['speaker']).extract(),
            'title': hxs.xpath(XPATHS['title']).extract(),
            'viewn': hxs.xpath(XPATHS['viewn']).extract()
        }
        newurl = '%s/transcript?language=en' % response.url
        yield Request(newurl, callback=self.parse_transcript, meta=meta)

    def parse_transcript(self, response):
        ''' parse transcript from TED talk transcript page
        '''
        item = TedtalkItem()
        hxs = response.selector

        transcript = hxs.xpath(XPATHS['transcript']).extract()

        item['speaker'] = response.meta['speaker']
        item['title'] = response.meta['title']
        item['viewn'] = response.meta['viewn']
        item['transcript'] = transcript

        return item
