# -*- coding: utf-8 -*-
"""
@Time ： 2023/2/13 20:29
@Auth ： 冯珂
@File ：FileService.py
@IDE ：PyCharm
@Motto: 
"""
import os

from flask import current_app

from Tool.OSS.upload_manage import UploadManage
from app.libs.error_code import ClientTypeError, Success, NotFound
from app.models.base import db
from app.models.oss_file import OssFile
from app.service.Base import BaseService


class FileService(BaseService):
    def upload(self):
        """
        文件上传
        :return:
        """
        files = self.get_files('files')
        if files is None:
            raise ClientTypeError(msg='无数据源！！！')
        is_private = int(self.get_form().get('is_private', 0))
        bucket = UploadManage()
        resource_id, key = bucket.private_upload(files, is_private)

        suffix = files.filename.split('.')[-1]  # 获取文件后缀名

        files.seek(0, os.SEEK_END)
        file_length = files.tell()

        # 数据写入数据库
        with db.auto_commit():
            file_obj = OssFile()
            file_obj.resource_id = resource_id
            file_obj.key = key
            file_obj.file_name = files.filename
            file_obj.file_extension = suffix
            file_obj.file_size = file_length
            file_obj.is_private = is_private
            db.session.add(file_obj)
        return Success(data={"key": None if is_private else key, "resource_id": resource_id})

    def down_file(self):
        """
        获取文件
        :return:
        """
        resource_id = self.get_data(key='resource_id')

        # 获取数据
        with db.auto_commit():
            file_query = db.session.query(OssFile).\
                filter(OssFile.resource_id == resource_id).first()
            if file_query is None:
                return NotFound(msg='没有找到该文件信息！！！')
            file = self.query_to_dict(file_query)
            # 判断是不是私有文件
            if file.get('is_private') == 1:
                key = file.get('key')
                bucket = UploadManage()
                url = bucket.get_oss_img(key=key)
            else:
                url = file.get('key')

        return Success(data={"url": url})

