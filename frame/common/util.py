#!/usr/bin/env python3.6
# -*- encoding=utf8 -*-
import time
from urllib.parse import unquote


class Util:
    @staticmethod
    def check_url (url: str, base_url: str) -> str:
        if not url.startswith("https://") or url.startswith("http://"):
            url = base_url + '/' + url
        try:
            url = unquote(url, 'utf8')
        except Exception:
            url = ''
        return url

    @staticmethod
    def stamp_time (time_str, fmt: str) -> int:
        tm = 0
        try:
            tim = time.mktime(time.strptime(time_str, fmt))
            tm = time.strftime("%Y%m%d%H%M", time.gmtime(tim))
        except:
            pass
        return tm

    @staticmethod
    def time_str_stamp (time_str, fmt: str) -> int:
        tm = 0
        try:
            tm = time.mktime(time.strptime(time_str, fmt))
        except:
            pass
        return tm

    @staticmethod
    def valid (field) -> bool:
        if (None is field) or ('' == field.strip()):
            return False
        return True

if __name__ == '__main__':
    tim = time.time()
    print (tim)
    tim = '2019-10-10'
    print (Util.stamp_time(tim, "%Y-%m-%d"))
    print (Util.time_str_stamp(tim, "%Y-%m-%d"))
    pass
