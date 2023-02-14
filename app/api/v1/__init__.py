# -*- coding: utf-8 -*-
"""
@Time ： 2023/2/13 15:45
@Auth ： 冯珂
@File ：__init__.py.py
@IDE ：PyCharm
@Motto: 
"""
from flask import Blueprint

from app.api.v1 import TestApi
from app.api.v1 import File


def create_blueprint_v1():
    """实例化蓝图"""
    bp_t = Blueprint('v1', __name__)
    TestApi.api.register(bp_t)
    File.api.register(bp_t)
    return bp_t