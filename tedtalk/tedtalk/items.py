# -*- coding: utf-8 -*-
import scrapy

XPATHS = {
    'title': '//span[@class="player-hero__title__content"]/text()',
    'speaker': '//span[@class="player-hero__speaker__content"]/text()',
    'viewn': '//div[@id="sharing-count"]/span/text()',
    'transcript': '//div[@class="talk-article__body talk-transcript__body"]' +
                  '//span[@class="talk-transcript__para__text"]//text()'
}


class TedtalkItem(scrapy.Item):
    ''' items scraped from tedtalk page
    '''
    title = scrapy.Field()
    speaker = scrapy.Field()
    viewn = scrapy.Field()
    transcript = scrapy.Field()
