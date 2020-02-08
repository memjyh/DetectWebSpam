# -*- coding: UTF-8 -*-
from scrapy.cmdline import execute

import os, sys

from time import sleep

from multiprocessing import Pool

sys.path.append(os.path.dirname(__file__))


# execute('scrapy crawl your_spider_name'.split(' '))


def run_spider(number):
    print('spider %s is started...' % number)
    print('scrapy runspider spamtest%s'%number+'.py')
    #execute(('scrapy runspider spamtest%s.py'%number).split(' '))  # 修改此处
    execute(('scrapy crawl spamtest%s --s LOG_FILE=spamtest%s.log'%(number,number)).split(' '))  # 修改此处


if __name__ == '__main__':
    '''
    p = Pool(3)

    for i in range(3):
        p.apply_async(run_spider, args=(i,))

        sleep(1)

    p.close()

    p.join()
    '''

    execute(('scrapy crawl spamtest0 --s LOG_FILE=spider0.log').split(' '))
