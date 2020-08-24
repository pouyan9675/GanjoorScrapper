# -*- coding: utf-8 -*-
import os

class SavingPipeline(object):

    def open_spider(self, spider):
        self.base_dir = 'output/'
    
    def process_item(self, item, spider):
        if 'm' not in item or len(item['m']) < 1:
            return None

        author_dir = self.base_dir + item['author'][0] + '/'
        if not os.path.exists(author_dir):
            os.makedirs(author_dir)

        with open(author_dir + item['source'] + '.txt', 'w', encoding='utf8') as txt:
            for i in range(0, len(item['m']), 2):
                txt.write(item['m'][i] + '\t\t' + item['m'][i+1]+'\n')

        return item
