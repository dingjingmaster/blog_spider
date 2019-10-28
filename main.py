#!/usr/bin/env python3.6
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

    """ http://xingzuo.piaoliang.com 开始 """
    # xz = spiderFactory.get_spider(COM_PIAOLIANG_NAME)
    # xz.set_seed_urls(xz_pl)
    # tpool.set_spider(xz)
    """ http://xingzuo.piaoliang.com 结束 """

    tpool.run()
    log.info('抓取任务完成!')
    exit(0)
