import json
import time

from flask import current_app

from Tool.Redis.Redis import Redis
from Tool.SMS.sms_base import Sms
from Tool.communal import random_int
from app.libs.enums import SmsTemplateTypeEnum
from app.libs.error_code import Success, ClientTypeError, SmsSendError
from app.service.Base import BaseService


class SmsService(BaseService):
    def send(self):
        data = self.get_data()
        sms_type = data.get('sms_type')
        phone = data.get('phone')
        if sms_type == 'register':
            # 先从redis数据库回去有效期验证码
            R = Redis()
            verification_str = R.get_str(mobile=phone)
            if verification_str:
                verification_dic = json.loads(verification_str)
                last_time = int(verification_dic.get('last_time'))
                today_count = verification_dic.get('today_count')
                if today_count == 5:
                    raise SmsSendError(msg="今天发送验证码次数上限！")
                if (last_time + 5 * 60) > time.time():
                    raise SmsSendError(msg="操作频繁，稍后再试！")
            else:
                verification_dic = {
                    'code': '',
                    'last_time': 0,
                    'today_count': 0
                }

            verification_dic['last_time'] = time.time()
            verification_dic['today_count'] += 1
            code = random_int(num=4)
            verification_dic['code'] = code
            R.set_str(mobile=phone, codes=json.dumps(verification_dic, ensure_ascii=False),
                      time=current_app.config['SMS_EXPIRATION'])

            template = SmsTemplateTypeEnum.注册.value
            template_code = template.get('sms_template_code')
            sign_name = template.get('sign_name')
            # 获取sms实例
            sms = Sms()
            sms.sms_send(template_code=template_code, phone_numbers=phone, data=verification_dic,
                         sign_name=sign_name)

            return Success(msg='验证码发送成功！')

        else:
            raise ClientTypeError()
