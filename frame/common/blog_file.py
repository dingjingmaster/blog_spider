#!/usr/bin/env python
# -*- encoding=utf8 -*-
import threading
import time

from frame.common.util import Util
from frame.log.log import log


class BlogFile(object):
    _mutex = threading.Lock()
    _rootdir = ''                                       # root dir 下保存本站所有索引信息,用于去重的
    _dir = ''                                           # dir 下保存具体每篇文章的信息，用于人工check

    def set_rootdir (self, rootdir: str):
        self._root_dir = obspath = os.path.abspath (rootdir)
        if os.path.exists(rootdir):
            if not os.path.isdir(obspath):
                log.error(self._name + '不合法的保存文件夹！')
                exit(1)
            if not os.access(obspath, os.R_OK | os.W_OK):
                log.error(self._name + '保存文件夹没有读写权限！')
                exit(1)
        else:
            os.mkdir(obspath)
        os.chmod(obspath, 0760)
        return self

    # 以name保存
    def set_dir (self, mdir: str):
        self._dir = obspath = os.path.abspath (self._rootdir + '/' + mdir)
        if os.path.exists(obspath):
            if not os.path.isdir(obspath):
                log.error(self._name + '不合法的保存文件夹！')
                return;
            if not os.access(obspath, os.R_OK | os.W_OK):
                log.error(self._name + '保存文件夹没有读写权限！')
                return;
        else:
            os.mkdir(obspath)
        os.chmod(obspath, 0760)
        return self

    """ 删除blog """
    def blog_delete (self, name) -> bool:
        try:
            os.rmdir(self._rootdir + '/' + name)
        except Exception as e:
            log.warn(str(e))
        return True

    """ 检测blog url 是否存在 """
    def blog_exist (self, name) -> bool:
        flag = False
        if os.path.exists(self._rootdir + '/' + name):
            flag = True
        return flag

    """ 检测img url 是否存在 """
    def image_exist (self, name:str, img:str) -> bool:
        flag = False
        if os.path.exists(self._rootdir + '/' + name + '/' + img):
            flag = True
        return flag

    """ 写入blog """
    def write_blog (self, url: str, title: str, tim: int, category: str, tag: str, spider: str, content: str, imgUrl: str):
        # 检查关键字段是否存在
        if (not Util.valid(title)) or (not Util.valid(spider) or (not Util.valid(url))):
            log.error ('title: %s spider: %s url: %s 参数错误!', title, spider, url)
            return False
        indexfile = self._dir + '/index.txt'
        with open(indexfile, os.O_RDWR | os.O_CREAT, 0660) as fw:
            fw.write('name:%s\n', title)
            fw.write('url:%s\n', url)
            fw.write('category:%s\n', category)
            fw.write('tag:%s\n', tag)
            fw.write('time:%s\n', tim)
            fw.write('spider:%s\n', spider)
            fw.write('img:%s\n', imgUrl)
        passagefile = self._dir + '%s.html' % name
        with open(indexfile, os.O_RDWR | os.O_CREAT, 0660) as fw:
            fw.write('<!Doctype html>
                        <html>
                            <head>
                                <title>%s</title>
                            </head>
                            <body>%s</body>
                        </html>' %
                        (name, content))
        return True

    """ 写入img """
    def write_image (self, url: str, name: str, extname: str, content: str):
        # 检查关键字段是否存在
        if not Util.valid(content) or pid <= 0:
            log.error('url=%s 信息错误!', url)
            return False
        imgfile = self._dir + '%s.%s' % (name, extname)
        with open(imgfile, os.O_RDWR | os.O_EXLOCK | os.O_CREAT | os.O_TRUNC, 0660) as fw:
            fw.write(content)
        return True


if __name__ == '__main__':
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
