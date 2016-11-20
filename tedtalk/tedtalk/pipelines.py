# -*- coding: utf-8 -*-
import json


class TedtalkPipeline(object):
    ''' store TedtalkItems in jsonl file
    '''
    def open_spider(self, spider):
        self.file = open('tedtalk.jl', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + '\n'
        self.file.write(line)
        return item
