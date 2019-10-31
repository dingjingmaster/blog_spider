#!/usr/bin/env python3.7
# -*- coding=utf-8 -*-

from frame.base.spider import Spider
from frame.common.param import *
from frame.log.log import log
from frame.parser_factory import get_parser

class COMLinuxidcSpider (Spider):
    def __init__ (self):
        self._name = COM_LINUXIDC_NAME
        self._webURL = COM_LINUXIDC_WEB_URL
        log.info('name:' + self._name + ' url:' + self._webURL + ' spider安裝成功!')

    def check (self):
        pass

    def run (self):
        parser = get_parser().get_parser(self._name)
        for url in self.get_passage_list():
            text = Spider.http_get(url)
            if '' == text:
                log.error('url:' + url + '抓取错误!')
                continue
            doc = parser.parse(text, rule='body>div>#middle .mframe>.wrapper>.mm')

            for ct in doc.children().items():
                pass
            print (doc.html())
            return;

