from alibabacloud_dysmsapi20170525.client import Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dysmsapi20170525 import models as dy_sms_api
from alibabacloud_tea_util import models as util_models
from flask import current_app

from app.libs.error_code import SmsSendError


class Sms:
    def __init__(self):
        pass

    @staticmethod
    def create_client(
        access_key_id: str,
        access_key_secret: str,
    ) -> Client:
        """
        使用AK&SK初始化账号Client
        @param access_key_id:
        @param access_key_secret:
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config(
            # 必填，您的 AccessKey ID,
            access_key_id=access_key_id,
            # 必填，您的 AccessKey Secret,
            access_key_secret=access_key_secret
        )
        # 访问的域名
        config.endpoint = f'dysmsapi.aliyuncs.com'
        return Client(config)

    def sms_send(self, template_code, phone_numbers, data, sign_name):
        client = self.create_client(access_key_id=current_app.config['ACCESS_KEY_ID'],
                                    access_key_secret=current_app.config['ACCESS_KEY_SECRET'])
        send_sms_request = dy_sms_api.SendSmsRequest(
            sign_name=sign_name,
            template_code=template_code,
            phone_numbers=str(phone_numbers),
            template_param=str(data)
        )
        runtime = util_models.RuntimeOptions()
        resp = client.send_sms_with_options(send_sms_request, runtime)
        if resp.status_code != 200 or resp.body.biz_id is None:
            raise SmsSendError(msg=resp.body.message)
