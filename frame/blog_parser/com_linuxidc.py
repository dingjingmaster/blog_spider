#!/usr/bin/env python
# -*- coding=utf-8 -*-
import re

import pyquery

from frame.base.parser import Parser
from frame.common.param import *
from frame.common.util import Util
from frame.log.log import log

class COMLinuxidcParser(Parser):
    __doc__ = """ https://www.linuxidc.com/linuxit/ """

    def __init__ (self):
        super().__init__()

    """ 書籍URL """
    def _parser_passage_title (self, doc: str) -> (bool, str):
        flag = False
        return flag, ''

    """ 標題 """
    def _parser_passage_url (self, doc: str) -> (bool, str):
        flag = False
        name = ''
        return flag, name.strip()

    """ 時間 """
    def _parser_passage_date (self, doc: str) -> (bool, str):
        flag = False
        return flag, ''

    """ 分類 """
    def _parser_passage_category (self, doc: str) -> (bool, str):
        flag = False
        return flag, ''

    """ 標籤 """
    def _parser_passage_tag (self, doc: str) -> (bool, str):
        flag = False
        return flag, ''

    """ 內容 """
    def _parser_massage_content (self, doc: str) -> (bool, str):
        flag = False
        return flag, ''

    """ 圖片 """
    def _parser_passage_img_url (self, doc: str) -> (bool, str, bytes):
        flag = False
        return flag, ''
