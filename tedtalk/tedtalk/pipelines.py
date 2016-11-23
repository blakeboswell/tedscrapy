# -*- coding: utf-8 -*-
import json


class TedtalkPipeline(object):
    ''' clean tedtalk item
    '''
    @staticmethod
    def unpack_singlet(l):
        [val] = l
        return val

    def parse_speaker(self, speaker):
        return self.unpack_singlet(speaker).replace(':', '').strip()

    def parse_viewn(self, viewn):
        val = self.unpack_singlet(viewn).replace(',', '').strip()
        try:
            return int(val)
        except:
            return val

    def parse_title(self, title):
        return self.unpack_singlet(title).strip()

    @staticmethod
    def parse_transcript(transcript):
        val = ' '.join([line.strip() for line in transcript
                       if len(line.strip()) > 0])
        return val.replace('\n', ' ')

    def process_item(self, item, spider):
        ''' clean and format TedtalkItem attributes
        '''
        item['speaker'] = self.parse_speaker(item['speaker'])
        item['viewn'] = self.parse_viewn(item['viewn'])
        item['title'] = self.parse_title(item['title'])
        item['transcript'] = self.parse_transcript(item['transcript'])
        return item


class WriteJsonl(object):
    ''' store TedtalkItems in jsonl file
    '''
    FILENAME = 'tedtalk.jl'

    def open_spider(self, spider):
        self.file = open(self.FILENAME, 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + '\n'
        self.file.write(line)
        return item
