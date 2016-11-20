# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

XPATHS = {
    'title': '//span[@class="player-hero__title__content"]/text()',
    'speaker': '//span[@class="player-hero__speaker__content"]/text()',
    'viewn': '//span[@class="talk-sharing__value"]/text()',
    'transcript': ''.join(
        ['//div[@class="talk-article__body talk-transcript__body"]',
         '//span[@class="talk-transcript__para__text"]//text()']
    )
}


class TedtalkItem(scrapy.Item):
    ''' item's scraped from tedtalk page
    '''
    title = scrapy.Field()
    speaker = scrapy.Field()
    viewn = scrapy.Field()
    transcript = scrapy.Field()
