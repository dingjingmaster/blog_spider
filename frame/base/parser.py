#!/usr/bin/env python3.6
# -*- encoding=utf8 -*-
import pyquery

"""
    需求字段：
        標題、發表日期、分類、標籤、內容、圖片
    
    需要的字段信息
        1. 网站根URL
        2. 解析器名字
        3. 解析器类型
            1. PARSER_PASSAGE_URL               文章URL
            2. PARSER_PASSAGE_TITLE             文章标题
            3. PARSER_PASSAGE_DATE              发表日期
            4. PARSER_PASSAGE_CATEGORY          文章分類
            5. PARSER_PASSAGE_TAG               文章標籤
            6. PARSER_PASSAGE_CONTENT           文章内容
            7. PARSER_PASSAGE_IMGURL            文章中的图片 URL
"""


class Parser(object):
    def __init__ (self):
        self._webURL = ''
        self._parserName = 'base_parser'

    def _parser_passage_url (self, doc: str) -> (bool, str):
        return

    def _parser_passage_title (self, doc: str) -> (bool, str):
        return

    def _parser_passage_date (self, doc: str) -> (bool, str):
        return

    def _parser_passage_category (self, doc: str) -> (bool, str):
        return

    def _parser_passage_tag (self, doc: str) -> (bool, str):
        return

    def _parser_passage_content (self, doc: str) -> (bool, str):
        return

    def _parser_passage_img_url (self, doc: str) -> (bool, str, bytes):
        return

    def get_parser_name (self):
        return self._parserName

    @staticmethod
    def _parser (doc: str, rule: str):
        return pyquery.PyQuery(doc).find(rule)

    def parse (self, doc: str, rule='', parse_type=-1):
        if self.PARSER_PASSAGE_URL == parse_type:
            if doc == '' or doc == None:
                return (False, '')
            return self._parser_passage_url(doc)
        elif self.PARSER_PASSAGE_TITLE == parse_type:
            if doc == '' or doc == None:
                return (False, '')
            return self._parser_passage_title(doc)
        elif self.PARSER_PASSAGE_DATE == parse_type:
            if doc == '' or doc == None:
                return (False, '')
            return self._parser_passage_date(doc)
        elif self.PARSER_PASSAGE_CATEGORY == parse_type:
            if doc == '' or doc == None:
                return (False, '')
            return self._parser_passage_category(doc)
        elif self.PARSER_PASSAGE_TAG == parse_type:
            if doc == '' or doc == None:
                return (False, '')
            return self._parser_passage_tag(doc)
        elif self.PARSER_PASSAGE_CONTENT == parse_type:
            if doc == '' or doc == None:
                return (False, '')
            return self._parser_passage_content(doc)
        elif self.PARSER_PASSAGE_IMGURL == parse_type:
            if doc == '' or doc == None:
                return (False, '')
            return self._parser_passage_img_url(doc)
        else:
            if doc == '' or doc == None:
                return (False, '')
            return Parser._parser(doc, rule)

    PARSER_PASSAGE_URL = 1
    PARSER_PASSAGE_TITLE = 2
    PARSER_PASSAGE_DATE = 3
    PARSER_PASSAGE_CATEGORY = 4
    PARSER_PASSAGE_TAG = 5
    PARSER_PASSAGE_CONTENT = 6
    PARSER_PASSAGE_IMGURL = 7
