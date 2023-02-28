# -*- coding: utf-8 -*-
"""
@Time ： 2023/2/3 10:54
@Auth ： 冯珂
@File ：TestApi.py
@IDE ：PyCharm
@Motto: 
"""
from flask import jsonify, request

from Tool.SMS.sms_base import Sms
from app.libs.enums import SmsTemplateTypeEnum
from app.libs.redprint import Redprint
from flask import request

api = Redprint('test')


@api.route('/get', methods=['GET'])
def test_get():
    a = Sms().sms_send(template_code=SmsTemplateTypeEnum.注册.value, phone_numbers='15606104652', data={"code": 8765},
                       sign_name=SmsTemplateTypeEnum.SignName_2.value)
    return jsonify({"test": "12"})
