#!/usr/bin/env python3.7
# -*- encoding=utf8 -*-

from frame.log.log import log
from frame.common.param import *
from frame.thread import ThreadPool
from frame.spider_factory import SpiderFactory

from url.com_linuxidc import blog_linuxidc

if __name__ == '__main__':
    log.info('抓取任务开始执行...')
    spiderFactory = SpiderFactory()
    tpool = ThreadPool()

    """ https://www.linuxidc.com 开始 """
    linuxidc = spiderFactory.get_spider (COM_LINUXIDC_NAME)
    linuxidc.set_seed_urls(blog_linuxidc)
    tpool.set_spider(linuxidc)
    """ https://www.linuxidc.com 结束 """

    tpool.run()
    log.info('抓取任务完成!')
    exit(0)
