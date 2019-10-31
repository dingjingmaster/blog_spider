#!/usr/bin/env python
# -*- coding=utf-8 -*-

""" 图片 """
class BlogImage():
    def __init__(self):
        self.__id = 0                       # 图片主键
        self.__url = ''                     # 图片URL
        self.__name = ''                    # 图片名字
        self.__extName = ''                 # 图片扩展名
        self.__content = ''                 # 图片内容


""" 博客文章 """
class BlogBean():
    def __init__(self, spiderName):
        self.__id = 0                       # 文章在数据库中的 ID
        self.__url = ''                     # 文章URL
        self.__title = ''                   # 标题
        self.__date = 0                     # 日期
        self.__category = ''                # 分类
        self.__tag = ''                     # 标签
        self.__content = ''                 # 内容 HTML/XML
        self.__sp = spiderName              # 爬虫名字
        self.__image = []                   # 图片

    def set_id(self, bid: int) -> BlogBean:
        if id >= 0:
            self.__id = bid
        return self

    def get_id(self) -> int:
        return self.__id

    def set_url(self, url: str) -> BlogBean:
        if '' != url and None != url:
            self.__url = url
        return self

    def get_url(self) -> str:
        return self.__url

    def set_title(self, title: str) -> BlogBean:
        if '' != title and None is not title:
            self.__title = title
        return self

    def get_title(self) -> str:
        return self.__title

    def set_date(self, date: int) -> BlogBean:
        if 0 > date:
            self.__date = date
        return self

    def get_date(self) -> int:
        return self.__date

    def set_category(self, cate: str) -> BlogBean:
        if '' != cate and None is not cate:
            self.__category = cate
        return self

    def get_category(self) -> str:
        return self.__category

    def set_tag(self, tag: str) -> BlogBean:
        if '' != tag and None is not tag:
            self.__tag = tag
        return self

    def get_tag(self) -> str:
        return self.__tag

    def set_spider_name(self, spider: str) -> BlogBean:
        if '' != spider and None is not spider:
            self.__sp = spider
        return self

    def get_spider_name(self) -> str:
        return self.__sp

    def append_image(self, image: BlogImage) -> BlogBean:
        self.__image.append(image)
        return self

    def yield_image(self):
        for img in self.__image:
            yield img

