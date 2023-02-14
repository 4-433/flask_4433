# -*- coding: utf-8 -*-
"""
@Time ： 2023/2/3 10:54
@Auth ： 冯珂
@File ：TestApi.py
@IDE ：PyCharm
@Motto: 
"""
from flask import jsonify, request
from app.libs.redprint import Redprint

api = Redprint('test')


@api.route('/get', methods=['GET'])
def test_get():
    return jsonify({"test": "12"})
