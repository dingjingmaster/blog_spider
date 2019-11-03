#!/usr/bin/env python
# -*- encoding=utf8 -*-
import threading
import time

import pymysql

from frame.common.util import Util
from frame.log.log import log


class BlogMysql(object):
    _mutex = threading.Lock()
    _host = ''
    _db = ''
    _port = 3306
    _user = ''
    _password = ''
    _connect = None

    def set_ip (self, host: str):
        self._host = host
        return self

    def set_port (self, port: int):
        self._port = port
        return self

    def set_database (self, db: str):
        self._db = db
        return self

    def set_usr (self, usr: str):
        self._user = usr
        return self

    def set_password (self, password: str):
        self._password = password
        return self

    def connect (self):
        self._connect = pymysql.Connect(
                host=self._host,
                port=self._port,
                user=self._user,
                db=self._db,
                passwd=self._password,
                charset='utf8'
        )
        return self

    """ 检测blog url 是否存在 """
    def blog_exist (self, url) -> bool:
        flag = False
        id = -1
        mysql = 'SELECT `id` FROM `blog_passage` WHERE url = "{url}"'.format(url=url)
        try:
            cursor = self._connect.cursor()
            cursor.execute(msql)
            self._connect.commit()
            result = cursor.fetchone()
            if None is not result:
                flag = True
        except Exception as e:
            log.error('MySQL 执行错误: ' + str(e))
        return flag

    """ 检测img url 是否存在 """
    def image_exist (self, url) -> bool:
        flag = False
        id = -1
        mysql = 'SELECT `id` FROM `blog_image` WHERE url = "{url}"'.format(url=url)
        try:
            cursor = self._connect.cursor()
            cursor.execute(msql)
            self._connect.commit()
            result = cursor.fetchone()
            if None is not result:
                flag = True
        except Exception as e:
            log.error('MySQL 执行错误: ' + str(e))
        return flag

    """ 插入blog """
    def insert_blog (self, url: str, title: str, tim: int, category: str, tag: str, spider: str, content: str):
        flag = False
        id = -1
        # 检查关键字段是否存在
        if (not Util.valid(title)) or (not Util.valid(spider) or (not Util.valid(url))):
            return flag, -1
        msql = 'INSERT INTO `blog_passage` (' \
               '`url`, `title`, `time`, `category`, `tag`, `spider`, `content`)' \
               ' VALUES ("{url}", "{title}", "{tim}", "{category}", "{tag}", "{spider}", "{content}");'.format( \
                title=self._connect.escape_string(title), tim=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(tim)),
                category=self._connect.escape_string(category), tag=self._connect.escape_string(tag),
                spider=self._connect.escape_string(spider), content=self._connect.escape_string(content));
        try:
            curosr = self._connect.cursor()
            curosr.execute(msql)
            self._connect.commit()
            id = int(curosr.lastrowid)
            if id >= 0:
                flag = True
                log.info('id=%d, name=%s 信息保存成功' % (id, title))
            else:
                log.error('name=%s 信息保存失败' % title)
        except Exception as e:
            log.error('MySQL 执行错误: ' + str(e))
        return flag, id

    """ 插入img """
    def insert_image (self, url: str, name: str, ext_name: str, context: str, pid: int):
        flag = False
        id = -1
        # 检查关键字段是否存在
        if (not Util.valid(name)) or (not Util.valid(content)):
            return flag, -1
        msql = 'INSERT INTO `blog_image` (' \
               '`url`, `name`, `ext_name`, `content`, `pid`)' \
               ' VALUES ("{url}", "{name}", "{ext_name}", "{content}", "{pid}");'.format( \
                name=self._connect.escape_string(name), ext_name=self._connect.escape_string(ext_name),
                content=self._connect.escape_string(content), pid=pid,
                url=self._connect.escape_string(url));
        try:
            curosr = self._connect.cursor()
            curosr.execute(msql)
            self._connect.commit()
            id = int(curosr.lastrowid)
            if id >= 0:
                flag = True
                log.info('id=%d, name=%s 信息保存成功' % (id, name))
            else:
                log.error('name=%s 信息保存失败' % name)
        except Exception as e:
            log.error('MySQL 执行错误: ' + str(e))
        return flag, id

    """ 读取blog """

    """ 读取img """


if __name__ == '__main__':
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
