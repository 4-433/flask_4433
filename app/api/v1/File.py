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
from app.validators.forms import FileGet

api = Redprint('file')


@api.route('/upload', methods=['POST'])
def file_upload():
    """
    上传文件
    :return:
    """
    res = FileService()
    return res.upload()


@api.route('/get', methods=['GET'])
def file_get():
    """
    通过resource_id获取文件url
    :return:
    """
    FileGet().validate_for_api()
    rm = FileService()
    return rm.down_file()
