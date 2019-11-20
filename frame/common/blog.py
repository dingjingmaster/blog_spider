#!/usr/bin/env python
# -*- coding=utf-8 -*-
import base64
import hashlib
import time

from frame.common.util import Util
from frame.common.blog_mysql import BlogMysql
from frame.common.param import *
from frame.log.log import log


""" 图片 """
class Image():
    def __init__(self):
        self.__id = 0                       # 图片主键
        self.__url = ''                     # 图片URL
        self.__name = ''                    # 图片名字
        self.__extName = ''                 # 图片扩展名
        self.__content = ''                 # 图片内容
        self.__pid = 0                      # 博客 id

    def set_id (self, iid: int):
        if iid >= 0:
            self.__id = iid
        return self

    def get_id (self):
        return self.__id

    def set_pid (self, iid: int):
        if iid >= 0:
            self.__pid = iid
        return self

    def get_pid (self):
        return self.__pid

    def set_url (self, url: str):
        if None is not url and '' != url:
            self.__url = url
        return self

    def get_url (self):
        return self.__url

    def get_name (self):
        return self.__name

    def set_name (self, name: str):
        if None is not name and '' != name:
            self.__name = name
        return self

    def get_ext_name (self):
        return self.__extName
    def set_ext_name (self, extName: str):
        if None is not extName and '' != extName:
            self.__extName = extName
        return self

    def set_content (self, content: str):
        if None is not content and '' != content:
            self.__content = content
        return self

    def get_content (self):
        return self.__content


""" 博客文章 """
class Blog ():
    def __init__(self, spiderName, save):
        self.__id = 0                       # 文章在数据库中的 ID
        self.__url = ''                     # 文章URL
        self.__title = ''                   # 标题
        self.__date = 0                     # 日期
        self.__category = ''                # 分类
        self.__tag = ''                     # 标签
        self.__content = ''                 # 内容 HTML/XML
        self.__sp = spiderName              # 爬虫名字
        self.__image = []                   # 图片

        self._save = save

        self.__mysql = None                 # 保存musql
        self.__dir = ''                     # 保存本地目录

        if 'file' == self._save:
            self.__dir
            pass
        elif 'mysql' == self._save:
            self.__mysql = BlogMysql()
            self.__mysql.set_ip(MYSQL_HOST)\
                .set_port(MYSQL_PORT)\
                .set_usr(MYSQL_USER)\
                .set_password(MYSQL_PASSWORD)\
                .set_database(MYSQL_BLOG_DB)\
                .connect()
        else:
            log.error ('不支持的数据保存方式!')
            exit(1)

    def exist (self, url: str):
        return self.__mysql.blog_exist(url)

    def save (self):
        pass

    def save_mysql (self):
        imgs = [i.get_url() for i in self.__image]
        # 检测信息是否存在
        if self.__mysql.blog_exist(self.get_url()):
            log.info ('文章: %s 已存在!', self.get_title())
            return True
        flag, bid = self.__mysql.insert_blog (self.get_url() , self.get_title(),\
                self.get_date(), self.get_category(), self.get_tag(), self.get_spider_name(),\
                self.get_content(), '|'.join(imgs))
        if not flag:
            return False
        # 检测图片是否存在
        for img in self.__image:
            if self.__mysql.image_exist(img.get_url()):
                log.info ('图片: %s 已存在!', self.get_url())
                continue
            flag, iid = self.__mysql.insert_image(img.get_url(), img.get_name(), img.get_ext_name(), img.get_content(), bid)
            if not flag:
                log.error ('图片: %s 保存失败!', img.get_url())
                self.__mysql.blog_delete (self.get_url())
                return False
        return True

    def set_id(self, bid: int):
        if id >= 0:
            self.__id = bid
        return self

    def get_id(self) -> int:
        return self.__id

    def set_url(self, url: str):
        if ('' != url) and (None is not url):
            self.__url = url
        return self

    def get_url(self) -> str:
        return self.__url

    def set_title(self, title: str):
        if ('' != title) and (None is not title):
            self.__title = title
        return self

    def get_title(self) -> str:
        return self.__title

    def set_date(self, date: int):
        if 0 < date:
            self.__date = date
        return self

    def get_date(self) -> int:
        return self.__date

    def set_category(self, cate: str):
        if '' != cate and None is not cate:
            self.__category = cate
        return self

    def get_category(self) -> str:
        return self.__category

    def set_tag(self, tag: str):
        if '' != tag and None is not tag:
            self.__tag = tag
        return self

    def get_tag(self) -> str:
        return self.__tag

    def set_content (self, content: str):
        if '' != content and None is not content:
            self.__content = content
        return self

    def get_content (self) -> str:
        return self.__content

    def set_spider_name(self, spider: str):
        if '' != spider and None is not spider:
            self.__sp = spider
        return self

    def get_spider_name(self) -> str:
        return self.__sp

    def append_image(self, image: Image):
        self.__image.append(image)
        return self

    def yield_image(self):
        for img in self.__image:
            yield img

    


