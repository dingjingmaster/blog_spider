#!/usr/bin/env python3.6
# -*- encoding=utf8 -*-
import time
from urllib.parse import unquote


class Util:
    @staticmethod
    def check_url (url: str, base_url: str) -> str:
        try:
            if not url.startswith("https://") or url.startswith("http://"):
                url = base_url + '/' + url
            url = unquote(url, 'utf8')
        except Exception:
            url = ''
        return url

    @staticmethod
    def stamp_time (timeInt) -> int:
        tm = 0
        try:
            tm = time.strftime("%Y%m%d%H%M", time.localtime(timeInt))
        except Exception as e:
            print(e)
            pass
        return int(tm)

    @staticmethod
    def time_str_stamp (time_str, fmt: str) -> int:
        tm = 0
        try:
            tm = time.mktime(time.strptime(time_str, fmt))
        except:
            pass
        return int(tm)

    @staticmethod
    def valid (field) -> bool:
        if (None is field) or ('' == field.strip()):
            return False
        return True

    @staticmethod
    def image_name(url: str):
        arr = url.split('/')
        if len(arr) <= 0:
            return "", ""
        name = arr[-1]
        arr = name.split('.')
        if len(arr) <= 1:
            return name, ""
        return arr[0], arr[1]

if __name__ == '__main__':
    tim = time.time()
    print (tim)
    print (Util.stamp_time(tim))
    print (Util.time_str_stamp(tim, "%Y-%m-%d"))
    pass
