from Tool.SMS.sms_base import Sms
from Tool.communal import random_int
from app.libs.enums import SmsTemplateTypeEnum
from app.libs.error_code import Success, ClientTypeError
from app.service.Base import BaseService


class SmsService(BaseService):
    def send(self):
        data = self.get_data()
        sms_type = data.get('sms_type')
        phone = data.get('phone')
        if sms_type == 'register':
            template = SmsTemplateTypeEnum.注册.value
            template_code = template.get('sms_template_code')
            sign_name = template.get('sign_name')
            code = random_int(num=4)
            # 写入redis

            data = {'code': code}
            # 获取sms实例
            sms = Sms()
            sms.sms_send(template_code=template_code, phone_numbers=phone, data=data, sign_name=sign_name)

            return Success(msg='验证码发送成功！')

        else:
            raise ClientTypeError()
