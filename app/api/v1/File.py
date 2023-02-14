# -*- coding: utf-8 -*-
"""
@Time ： 2023/2/13 15:59
@Auth ： 冯珂
@File ：File.py
@IDE ：PyCharm
@Motto: 
"""
from app.libs.redprint import Redprint
from app.service.File.FileService import FileService

api = Redprint('file')


@api.route('/upload', methods=['POST'])
def file_upload():
    """
    上传文件
    :return:
    """
    res = FileService()
    return res.upload()
