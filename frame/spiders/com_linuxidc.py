#!/usr/bin/env python3.7
# -*- coding=utf-8 -*-

from frame.log.log import log
from frame.common.param import *
from frame.common.util import Util
from frame.base.spider import Spider
from frame.common.blog import Blog, Image
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
            text = Spider.http_get (url)
            if '' == text:
                log.error('url:' + url + '抓取错误!')
                continue
            doc = parser.parse(text, rule='body>div>#middle .mframe>.wrapper>.mm')
            for ct in doc.children().items():
                blog = Blog (self._name)
                # 解析博客 URL
                flag, blogUrl = parser.parse(ct, parse_type=parser.PARSER_PASSAGE_URL)
                if not flag:
                    log.error('url:' + url + '解析 url 错误!')
                    continue
                blogUrl = Util.check_url (blogUrl, self._webURL)
                print (flag)
                print (blogUrl)

                # 解析博客 标题
                flag, blogTitle = parser.parse(ct, parse_type=parser.PARSER_PASSAGE_TITLE)
                if not flag:
                    log.error('url:' + url + '解析 title 错误!')
                    continue
                print (flag)
                print (blogTitle)

                # 解析博客 内容
                content = Spider.http_get (blogUrl)
                if '' == content:
                    log.error('url:' + blogUrl + '获取内容错误!')
                    continue
                flag, blogContent = parser.parse(content, parse_type=parser.PARSER_PASSAGE_CONTENT)
                if not flag:
                    log.error('url:' + blogUrl + '解析内容错误!')
                    continue

                print (flag)
                print (blogContent)

                print (ct.html())
                print ('<-------------------------------------------------------------------->')
                return;
                exit (0)
            exit (0)

