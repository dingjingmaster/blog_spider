#!/usr/bin/env python3.6
# -*- encoding=utf8 -*-
from frame.common.param import *
from frame.blog.com_xzw import COMXzwParser
from frame.blog.net_d1xz import NTD1zxParser
from frame.blog.com_piaoliang import CMPiaoliangParser


class ParserFactory:
    def get_parser (self, parser_name: str):
        if parser_name in self._parserDict:
            return self._parserDict[parser_name]

    _parserDict = {
        COM_XZW_NAME:       COMXzwParser(),
        NET_D1XZ_NAME:      NTD1zxParser(),
        COM_PIAOLIANG_NAME: CMPiaoliangParser(),
    }


_parser = ParserFactory()


def get_parser ():
    return _parser
