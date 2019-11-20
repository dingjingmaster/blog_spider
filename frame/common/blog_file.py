#!/usr/bin/env python3.8
# -*- encoding=utf8 -*-
import os
import time
import hashlib
import threading

from frame.common.util import Util
from frame.log.log import log


class BlogFile(object):
    _rootdir = ''                                       # root dir 下保存本站所有索引信息,用于去重的
    _dir = ''                                           # dir 下保存具体每篇文章的信息，用于人工check

    def set_rootdir (self, rootdir: str):
        self._rootdir = obspath = os.path.abspath (rootdir)
        if os.path.exists(obspath):
            if not os.path.isdir(obspath):
                log.error('不合法的保存文件夹！')
                return
            if not os.access(obspath, os.R_OK | os.W_OK):
                log.error('保存文件夹没有读写权限！')
                return
        else:
            os.makedirs(obspath)
        return self

    # 以url保存
    def set_dir (self, url: str):
        mdir = hashlib.md5(url.encode('utf-8')).hexdigest()
        self._dir = obspath = os.path.abspath (self._rootdir + '/' + mdir)
        if os.path.exists(obspath):
            if not os.path.isdir(obspath):
                log.error('不合法的保存文件夹！')
                return;
            if not os.access(obspath, os.R_OK | os.W_OK):
                log.error('保存文件夹没有读写权限！')
                return;
        else:
            os.mkdir(obspath)
        return self

    """ 删除blog """
    def blog_delete (self, url) -> bool:
        name = hashlib.md5(url.encode('utf-8')).hexdigest()
        bpath = self._rootdir + '/' + name
        try:
            os.rmdir(bpath)
        except Exception as e:
            log.warn(str(e))
        log.info('blog %s 删除成功！' % bpath)
        return True

    """ 检测blog url 是否存在 """
    def blog_exist (self, url) -> bool:
        flag = False
        name = hashlib.md5(url.encode('utf-8')).hexdigest()
        if os.path.exists(self._dir + '/index.txt'):
            log.info('blog %s 已存在！' % self._dir)
            flag = True
        return flag

    """ 检测img url 是否存在 """
    def image_exist (self, url:str) -> bool:
        #flag = False
        #name = hashlib.md5(url.encode('utf-8')).hexdigest()
        #imgpath = self._dir + '/' + name 
        #if os.path.exists(imgpath):
        #    log.info('blog %s 已存在！' % imgpath)
        #    flag = True
        #return flag
        return False

    """ 写入blog """
    def write_blog (self, url: str, title: str, tim: int, category: str, tag: str, spider: str, content: str, imgUrl: str):
        # 检查关键字段是否存在
        if (not Util.valid(title)) or (not Util.valid(spider) or (not Util.valid(url))):
            log.error ('title: %s spider: %s url: %s 参数错误!', title, spider, url)
            return False, 1
        indexfile = self._dir + '/index.txt'
        log.info('blog index %s 已存在！' % indexfile)
        with open(indexfile, 'w+') as fw:
            fw.write('name:%s\n' % title)
            fw.write('url:%s\n' % url)
            fw.write('category:%s\n' % category)
            fw.write('tag:%s\n' % tag)
            fw.write('time:%s\n' % tim)
            fw.write('spider:%s\n' % spider)
            fw.write('img:%s\n' % imgUrl)
        passagefile = self._dir + '/%s.html' % title
        log.info('blog passage %s 已存在！' % passagefile)
        with open(passagefile, 'w+') as fw:
            fw.write('<!Doctype html> \
                        <html> \
                            <head> \
                                <title>%s</title> \
                            </head> \
                            <body>%s</body> \
                        </html>' %
                        (title, content))
        return True, 1

    """ 写入img """
    def write_image (self, name: str, extname: str, content: str, url:str, pid: int):
        # 检查关键字段是否存在
        if not Util.valid(content) or pid < 0:
            log.error('url=%s 信息错误!', url)
            return False, 0
        n = hashlib.md5(url.encode('utf-8')).hexdigest()
        imgfile = self._dir + '/%s.%s' % (n, extname)
        with open(imgfile, 'wb+') as fw:
            fw.write(content)
        return True, 1


if __name__ == '__main__':
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
