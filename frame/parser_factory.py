#!/usr/bin/env python3.7
# -*- encoding=utf8 -*-
from frame.common.param import *
from frame.blog_parser.com_linuxidc import COMLinuxidcParser


class ParserFactory:
    def get_parser (self, parser_name: str):
        if parser_name in self._parserDict:
            return self._parserDict[parser_name]

    _parserDict = {
            COM_LINUXIDC_NAME : COMLinuxidcParser()
    }


_parser = ParserFactory()


def get_parser ():
    return _parser
