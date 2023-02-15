# -*- coding: utf-8 -*-
"""
@Time ： 2023/2/13 20:29
@Auth ： 冯珂
@File ：FileService.py
@IDE ：PyCharm
@Motto: 
"""
import os

from Tool.OSS.upload_manage import UploadManage
from app.libs.error_code import ClientTypeError, Success
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
        is_private = self.get_form().get('is_private', 0)
        bucket = UploadManage()
        key = bucket.private_upload(files, is_private)
        suffix = files.filename.split('.')[-1]  # 获取文件后缀名

        files.seek(0, os.SEEK_END)
        file_length = files.tell()

        # 数据写入数据库
        with db.auto_commit():
            file_obj = OssFile()
            file_obj.key = key
            file_obj.file_name = files.filename
            file_obj.file_extension = suffix
            file_obj.file_size = file_length
            file_obj.is_private = is_private
            db.session.add(file_obj)
        return Success(data={"key": key})

