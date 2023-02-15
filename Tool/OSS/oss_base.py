# -*- coding: utf-8 -*-
"""
@Time ： 2023/2/13 16:43
@Auth ： 冯珂
@File ：oss_base.py
@IDE ：PyCharm
@Motto: 
"""
import oss2
import uuid
from flask import current_app

from Tool.communal import get_int_now


class OssBase:
    def __init__(self):
        # config
        self._bucket = current_app.config['OSS_BUCKET']
        self._access_key_id = current_app.config['ACCESS_KEY_ID']
        self._access_key_secret = current_app.config['ACCESS_KEY_SECRET']

        #
        self._outer_endpoint = current_app.config['OSS_ENDPOINT']

    @property
    def auth(self):
        return oss2.Auth(self._access_key_id, self._access_key_secret)

    def get_bucket(self):
        return oss2.Bucket(self.auth, self._outer_endpoint, self._bucket)

    @staticmethod
    def gen_key(file_name):
        """
        生成文件保存的key
        :param file_name: 文件名
        :return:
        """
        if not file_name:
            return None
        ext = file_name.split('.')[1].lower()  # 后缀名
        name = file_name.split('.')[0]
        if not ext:
            return None
        int_date = get_int_now()
        uuidstr = str(uuid.uuid1()).replace('-', '')

        name = "%s%s/%s.%s" % (int_date, uuidstr, name, ext)
        return name
