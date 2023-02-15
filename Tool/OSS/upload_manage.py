# -*- coding: utf-8 -*-
"""
@Time ： 2023/2/13 23:14
@Auth ： 冯珂
@File ：upload_manage.py
@IDE ：PyCharm
@Motto: 
"""
import oss2
from flask import current_app

from Tool.OSS.oss_base import OssBase

from app.libs.error_code import FileError


class UploadManage(OssBase):
    def private_upload(self, content, is_private=0):
        """
        上传文件
        :param content: 文件流
        :param is_private: 是否私有：0：公有，1：私有
        :return:
        """
        file_name = content.filename  # 文件原始名称
        key = self.gen_key(file_name)

        bucket = self.get_bucket()

        headers = {}
        headers.update({"x-oss-object-acl": oss2.OBJECT_ACL_PRIVATE if is_private else oss2.OBJECT_ACL_PUBLIC_READ})
        res = bucket.put_object(key, content, headers)
        if res.status == 200:
            if is_private == 0:
                return r'{}/{}?type=new'.format(current_app.config['FILE_URL'], key)
            else:
                return key
        raise FileError(msg="文件上传错误！")
